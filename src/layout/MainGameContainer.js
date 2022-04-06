/* eslint-plugin-disable jsx-a11y */
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
import { AnswersContainer, GameSummary } from './Layout';

function MainGameContainer() {
    /* MAINGAMECONTAINER will launch a modal once the game ends */

    const [sessionLevels, setSessionLevels] = useState(undefined);

    // Configure game session state
    const [currentLevelIndex, setCurrentLevelIndex] = useState(0);
    const [gameIsFinished, setGameIsFinished] = useState(false);
    const [gameIsWon, setGameIsWon] = useState(undefined);
    const [accumulatedPrize, setAccumulatedPrize] = useState(0);

    // Game management functions
    const increasePrize = (prize) => {
        setAccumulatedPrize(
            (prevAccumulatedPrize) => prevAccumulatedPrize + prize
        );
    };

    const handleAnswerSelection = (clickedAnswer) => {
        setTimeout(() => {
            if (!clickedAnswer) {
                // If wrong answer is chosen, player looses everything and game finishes
                setAccumulatedPrize(0);
                setGameIsFinished(true);
                setGameIsWon(false);
            } else {
                // If correct answer is chosen
                increasePrize(sessionLevels[currentLevelIndex].prize);

                if (currentLevelIndex === sessionLevels.length - 1) {
                    // If current level is the last one.
                    setGameIsFinished(true);
                    setGameIsWon(true);
                } else {
                    // If correct answer is chosen but current level isn't the last one

                    setCurrentLevelIndex(
                        (prevCurrentLevelIndex) => prevCurrentLevelIndex + 1
                    );
                }
            }
        }, 300);
    };

    const voluntaryEndGame = () => {
        setGameIsFinished(true);
    };

    useEffect(() => {
        const fetchLevels = async () => {
            const res = await fetch('http://localhost:5000/api/questions/');
            const data = await res.json();

            setSessionLevels(data);
        };

        fetchLevels();
    }, []);

    return (
        <div>
            {sessionLevels === undefined ? (
                <p>Wait</p>
            ) : gameIsFinished ? (
                <GameSummary
                    gameResult={gameIsWon}
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
                            onClick={() => voluntaryEndGame()}
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
