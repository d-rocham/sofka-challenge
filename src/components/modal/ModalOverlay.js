/* eslint import/no-cycle: [0] */

/* eslint-plugin-disable jsx-a11y */

import React from 'react';

function ModalOverlay() {
    return (
        <div className="h-screen w-screen fixed top-0 left-0 z-50 bg-gray-500 opacity-50" />
    );
}

export default ModalOverlay;
