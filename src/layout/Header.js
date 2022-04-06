import React from 'react';
import { IoMdClock, IoMdSettings } from 'react-icons/io';

function Header() {
    return (
        <div className="Header w-full sticky top-0 bg-sky-600 mb-3">
            <div className="Header-Flex-Container p-2 flex flex-row justify-evenly items-center text-white">
                <IoMdClock className="text-4xl" />
                <h2 className="HeaderTitle grow font-ubuntu font-medium text-4xl ">
                    MILLONARIO
                </h2>
                <IoMdSettings className="text-4xl" />
            </div>
        </div>
    );
}

export default Header;
