import React from 'react';
import './App.css';
import Header from './layout/Layout';
import MainGameContainer from './layout/MainGameContainer';

function App() {
    return (
        <div className="App">
            <Header />
            <MainGameContainer />
        </div>
    );
}

export default App;
