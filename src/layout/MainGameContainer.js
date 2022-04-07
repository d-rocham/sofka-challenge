/* eslint-plugin-disable jsx-a11y */
/* eslint no-nested-ternary: [0] */
/* eslint no-nested-ternary: [0] */
/* eslint no-unused-vars: [1] */
/* eslint no-lone-blocks: [0] */
/* eslint import/no-cycle: [0] */

import { React, useEffect, useState } from 'react';
import {
    GameInfoCard,
    QuestionCard
} from '../components/InformationDisplay/InformationDisplay';
import LoadingSpinner from '../components/loadingSpinner';
import { AnswersContainer, GameSummary } from './Layout';

function MainGameContainer() {
    // Game Session levels
    const [sessionLevels, setSessionLevels] = useState(undefined);

    // Fetch server for random levels upon page load
    useEffect(() => {
        const fetchLevels = async () => {
            const res = await fetch('http://127.0.0.1:5000/api/questions/');
            const data = await res.json();

            setSessionLevels(data);
        };

        fetchLevels();
    }, []);

    // Configure game session states
    const [currentLevelIndex, setCurrentLevelIndex] = useState(0);
    const [gameIsFinished, setGameIsFinished] = useState(undefined);
    /* undefined = not finished
        0 = lost
        1 = abandoned
        2 = won
    */
    // const [gameIsWon, setGameIsWon] = useState(undefined);
    const [accumulatedPrize, setAccumulatedPrize] = useState(0);

    // Game management functions
    const increasePrize = (prize) => {
        setAccumulatedPrize(
            (prevAccumulatedPrize) => prevAccumulatedPrize + prize
        );
    };

    const handleAnswerSelection = (clickedAnswer) => {
        // Give user a small wait to see color change on clicked answer
        setTimeout(() => {
            if (!clickedAnswer) {
                // If wrong answer is chosen, player looses everything and game finishes
                setAccumulatedPrize(
                    (prevAccumulatedPrize) =>
                        prevAccumulatedPrize - prevAccumulatedPrize
                );
                setGameIsFinished(0);
            } else {
                // If correct answer is chosen
                increasePrize(sessionLevels[currentLevelIndex].prize);

                if (currentLevelIndex === sessionLevels.length - 1) {
                    // If current level is the last one.
                    setGameIsFinished(2);
                } else {
                    // If correct answer is chosen but current level isn't the last one
                    setCurrentLevelIndex(
                        (prevCurrentLevelIndex) => prevCurrentLevelIndex + 1
                    );
                }
            }
        }, 300);
    };

    /* Due to useState hook stale closure, accumulatedPrize doesn't update when user selects wrong answer.
    Thus, useEffect is used. More info in https://dmitripavlutin.com/react-hooks-stale-closures/ */

    useEffect(() => {
        const saveResultsInLocalStorage = () => {
            const gameKey = 'sofka-challenge-player';
            const getGameInfo = () => localStorage.getItem(gameKey);

            const resultsObject = {
                finalPrize: accumulatedPrize,
                result:
                    gameIsFinished === 1
                        ? 'Abandonaste'
                        : gameIsFinished === 2
                        ? 'Ganaste'
                        : 'Perdiste'
            };

            // Check if gameKey already exists in localStorage. Prevent overwriting it
            const gameLocalStorage = getGameInfo();

            if (!gameLocalStorage) {
                localStorage.setItem(gameKey, JSON.stringify([resultsObject]));
            } else {
                const currentInfo = JSON.parse(getGameInfo());

                currentInfo.push(resultsObject);

                localStorage.setItem(gameKey, JSON.stringify(currentInfo));
            }
        };
        if (gameIsFinished !== undefined) {
            saveResultsInLocalStorage();
        }
    }, [gameIsFinished]);

    return (
        <div>
            {sessionLevels === undefined ? (
                <LoadingSpinner />
            ) : gameIsFinished !== undefined ? (
                <GameSummary
                    gameResult={gameIsFinished}
                    finalPrize={accumulatedPrize}
                />
            ) : (
                <div className="Board-Container flex flex-col mt-3 px-2">
                    <GameInfoCard
                        currentLevel={currentLevelIndex + 1}
                        accumulatedPrize={accumulatedPrize}
                        levelPrize={sessionLevels[currentLevelIndex].prize}
                    />
                    <QuestionCard
                        questionText={
                            sessionLevels[currentLevelIndex].questions
                                .question_text
                        }
                    />
                    <AnswersContainer
                        answers={
                            sessionLevels[currentLevelIndex].questions.answers
                        }
                        handleSelection={handleAnswerSelection}
                    />

                    {accumulatedPrize > 0 ? (
                        <div
                            className="bg-orange-400 text-white font-ubuntu font-medium text-xl mx-2 mt-6 py-2 hover:cursor-pointer"
                            onClick={() => setGameIsFinished(1)}
                        >
                            Retirarme con mi premio
                        </div>
                    ) : (
                        ''
                    )}
                </div>
            )}
        </div>
    );
}

export default MainGameContainer;
