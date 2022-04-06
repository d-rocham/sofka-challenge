import React from 'react';

function GameInfoCard({ currentLevel, accumulatedPrize, levelPrize }) {
    return (
        <div className="bg-slate-100 p-2 mb-3 font-ubuntu font-normal text-lg text-left text-black">
            <p>{`Estás en el nivel ${currentLevel}`}</p>
            <p>{`Llevas $${accumulatedPrize} acumulados`}</p>
            <p>{`En este nivel obtendrás $${levelPrize} adicionales`}</p>
        </div>
    );
}

export default GameInfoCard;
