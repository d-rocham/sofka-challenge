import { useDebugValue, useState } from 'react';

/**
 * Custom hook for using Modal component
 * @returns {Object} isVisible (boolean), toggleModal (function)
 */
const useModal = () => {
    const [isVisible, setIsVisible] = useState(false);

    const toggleModal = () => {
        setIsVisible(!isVisible);
    };

    useDebugValue();

    return {
        isVisible,
        toggleModal
    };
};

export default useModal;
