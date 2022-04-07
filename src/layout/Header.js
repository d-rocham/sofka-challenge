/* eslint no-unused-vars: [1] */

import React from 'react';
import { IoMdClock } from 'react-icons/io';
import { ResultsModal } from '../components/InformationDisplay/InformationDisplay';
import { ModalComponent, useModal } from '../components/modal/Modal';

function Header() {
    const ShowResultsModal = useModal();

    return (
        <div className="Header w-full sticky top-0 bg-sky-600 mb-3">
            <div className="Header-Flex-Container p-2 flex flex-row justify-between items-center text-white">
                <h2 className="HeaderTitle pl-2 font-ubuntu font-medium text-4xl ">
                    MILLONARIO
                </h2>
                <IoMdClock
                    className="text-4xl hover:cursor-pointer"
                    onClick={() => ShowResultsModal.toggleModal()}
                />
            </div>
            <ModalComponent
                isVisible={ShowResultsModal.isVisible}
                hideModal={ShowResultsModal.toggleModal}
            >
                <ResultsModal />
            </ModalComponent>
        </div>
    );
}

export default Header;
