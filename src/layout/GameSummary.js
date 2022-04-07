/* eslint-plugin-disable jsx-a11y */

/* eslint no-unused-vars: [1] */
/* eslint no-nested-ternary: [0] */

import React from 'react';

function GameSummary({ gameResult, finalPrize = null }) {
    // gameResult undefined for retirado, true for won, false for fucked up
    return (
        <div>
            <h2 className="font-ubuntu text-6xl">
                {gameResult === 1
                    ? 'Te retiraste'
                    : gameResult === 2
                    ? 'Ganaste'
                    : 'Has perdido'}
            </h2>
            <br />
            <div>
                {gameResult === 1 || gameResult === 2 ? (
                    <div>
                        <p className="font-ubuntu text-4xl">{`Te llevas a casa ${finalPrize}`}</p>
                    </div>
                ) : (
                    <p className="font-ubuntu text-xl">
                        Mejor suerte en una próxima oportunidad
                    </p>
                )}
            </div>
            <div
                className="bg-orange-400 text-white font-ubuntu font-medium text-xl mx-2 mt-6 md:mt-4 py-2 hover:cursor-pointer md:w-96 md:my-0 md:mx-auto"
                onClick={() => window.location.reload(true)}
            >
                ¡Jugar de nuevo!
            </div>
        </div>
    );
}

export default GameSummary;
