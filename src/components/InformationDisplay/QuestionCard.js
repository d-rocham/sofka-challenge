import React from 'react';

function QuestionCard({ questionText }) {
    return (
        <div className="bg-blue-600 font-ubuntu text-white text-2xl p-2 mb-3">
            <p>{questionText}</p>
        </div>
    );
}

export default QuestionCard;
