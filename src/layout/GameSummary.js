/* eslint no-unused-vars: [1] */
/* eslint no-nested-ternary: [0] */

import React from 'react';

function GameSummary({ gameResult, finalPrize = null }) {
    // gameResult undefined for retirado, true for won, false for fucked up
    return (
        <div>
            <h2 className="font-ubuntu text-6xl">
                {gameResult === undefined
                    ? 'Te retiraste'
                    : gameResult
                    ? 'Ganaste'
                    : 'Has perdido'}
            </h2>
            <br />
            <div>
                {gameResult === undefined || gameResult === true ? (
                    <div>
                        <p className="font-ubuntu text-4xl">{`Te llevas a casa ${finalPrize}`}</p>
                    </div>
                ) : (
                    <p className="font-ubuntu text-xl">
                        Mejor suerte en una próxima oportunidad
                    </p>
                )}
            </div>
        </div>
    );
}

export default GameSummary;
