import React from 'react';
import { AnswerCard } from '../components/InformationDisplay/InformationDisplay';

function AnswersContainer({ answers, handleSelection }) {
    return (
        <div className="flex flex-col gap-2 px-2">
            {answers.map((answer) => (
                <AnswerCard
                    text={answer.answer_text}
                    isCorrect={answer.correct}
                    handleSelection={handleSelection}
                    key={answer.id}
                />
            ))}
        </div>
    );
}

export default AnswersContainer;
