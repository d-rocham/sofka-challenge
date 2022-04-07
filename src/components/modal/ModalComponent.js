/* eslint-plugin-disable jsx-a11y */
/* eslint import/no-cycle: [0] */

import React from 'react';
import { createPortal } from 'react-dom';
import { ModalOverlay } from './Modal';

function Modal({ children, isVisible, hideModal }) {
    return isVisible
        ? createPortal(
              <>
                  <ModalOverlay />
                  <div className="fixed top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 z-50 h-full w-screen overflow-y-auto p-2 md:w-96">
                      <div className="flex flex-col gap-1">
                          {children}
                          <button
                              type="button"
                              className="bg-white font-ubuntu font-medium py-2 text-xl text-sky-600"
                              onClick={hideModal}
                          >
                              Cerrar
                          </button>
                      </div>
                  </div>
              </>,
              document.body
          )
        : null;
}

export default Modal;
