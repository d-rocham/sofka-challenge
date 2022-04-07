/* eslint no-unused-vars: [1] */

import React from 'react';

function ResultsModal() {
    const gameRecords = JSON.parse(
        localStorage.getItem('sofka-challenge-player')
    );

    return (
        <div className="bg-white pb-3">
            <h3 className="font-ubuntu text-4xl text-center text-sky-600 py-2">
                Tus resultados
            </h3>
            {gameRecords === null ? (
                <p className="text-center">Aún no has jugado!</p>
            ) : (
                <ol className="list-decimal pl-8 font-ubuntu text-lg ">
                    {gameRecords.map((record) => (
                        <li>
                            {' '}
                            <p className="font-ubuntu text-lg">{`${record.result} con $${record.finalPrize}`}</p>
                        </li>
                    ))}
                </ol>
            )}
        </div>
    );
}

export default ResultsModal;
