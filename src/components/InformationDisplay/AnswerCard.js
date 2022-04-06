/* eslint-plugin-disable jsx-a11y */

/* eslint no-nested-ternary: [0] */
/* eslint no-nested-ternary: [0] */
/* eslint no-unused-vars: [1] */

import React, { useState } from 'react';

function AnswerCard({ text, isCorrect, handleSelection }) {
    const [isClicked, setIsClicked] = useState(false);

    const handleClick = () => {
        setIsClicked((prevIsClicked) => !prevIsClicked);
        handleSelection(isCorrect);
    };

    return (
        <div
            className={`${
                !isClicked
                    ? 'bg-amber-300'
                    : isCorrect
                    ? 'bg-lime-300'
                    : 'bg-red-300'
            } font-ubuntu text-xl py-2 hover:cursor-pointer`}
            onClick={() => handleClick()}
        >
            <p>{text}</p>
        </div>
    );
}

export default AnswerCard;
