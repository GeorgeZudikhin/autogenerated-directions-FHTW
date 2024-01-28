import React, { useState, useEffect } from 'react';
import { useLocation } from 'react-router-dom';
import logo from './assets/Logo.jpg';
import fhtwlogo from  './assets/fhtw_logo.svg.png';
import adiobook from  './assets/audiobook.PNG';
import aplus from  './assets/aplus.PNG';
import aminus from  './assets/aminus.PNG';
import bnw from  './assets/black&white.PNG';
import farbe from  './assets/farbe.PNG';
import znormal from  './assets/znormal.PNG';
import zplus from  './assets/zplus.PNG';
import returnz from  './assets/return.PNG';
import sprache from  './assets/sprache.PNG';
import { Link } from 'react-router-dom';

function App2(){
  const location = useLocation();
  const { startNode, endNode, pathDescription } = location.state || {};
  const pathInfo = startNode && endNode ? `${startNode} -> ${endNode}` : 'No path information available';
  console.log("Path Description in App2:", pathDescription);
  const [contrastMode, setContrastMode] = useState(false);
  const [fontSize, setFontSize] = useState(16); // Initial font size of 16px
  const [lineHeight, setLineHeight] = useState(1.5); // Initial line height
  const [reset] = useState(1.5); // Initial line height
  const [fontSizeCounter, setFontSizeCounter] = useState(0);
  const [lineHeightCounter, setLineHeightCounter] = useState(0);

//Contrast
const toggleContrast = () => {
  setContrastMode(!contrastMode);
  if (!contrastMode) {
    document.body.style.backgroundColor = '#000000';
    document.body.style.color = '#ffffff';

    // Change text color to white for all elements with class 'contrastable-text'
    const contrastableTextElements = document.querySelectorAll('.contrastable-text');
    contrastableTextElements.forEach(element => {
      element.style.color = '#ffffff';
    });
  } else {
    document.body.style.backgroundColor = '#ffffff';
    document.body.style.color = '#000000';

    // Reset text color for all elements with class 'contrastable-text'
    const contrastableTextElements = document.querySelectorAll('.contrastable-text');
    contrastableTextElements.forEach(element => {
      element.style.color = ''; // Reset to default or your desired color
    });
  }
};

const resetContrast = () => {
  setContrastMode(false);
  document.body.style.backgroundColor = '#ffffff';
  document.body.style.color = '#000000';
  // Reset text color for all elements with class 'contrastable-text'
  const contrastableTextElements = document.querySelectorAll('.contrastable-text');
  contrastableTextElements.forEach(element => {
      element.style.color = ''; // Reset to default or your desired color
  });
};

//Font
const increaseFontSize = () => {
  if (fontSizeCounter < 5) {
    setFontSize(fontSize => fontSize + 4);
    setFontSizeCounter(counter => counter + 1);
  }
};

const decreaseFontSize = () => {
  if (fontSizeCounter > 0) {
    setFontSize(fontSize => fontSize - 4);
    setFontSizeCounter(counter => counter - 1);
  }
};

//LineHeight
const increaseLineHeight = () => {
  if (lineHeightCounter < 5) {
      setLineHeight(lineHeight=>lineHeight + 0.2);
      setLineHeightCounter(counter => counter + 1);
  }
};  

useEffect(() => {
  const handleKeyPress = (event) => {
      if (event.target.tagName === 'INPUT' || event.target.tagName === 'TEXTAREA') {
          return;
      }

      switch(event.key) {
          case '+':
              increaseFontSize(); // increases the font size
              break;
          case '-':
              decreaseFontSize(); // resets the font size
              break;
          case 'c':
              toggleContrast(); // changes the contrast
              break;
          case 'd':
              resetContrast(); // resets the contrast
              break;
          case 'z':
              increaseLineHeight(); // increases the line spacing
              break;
          case 't':
              resetLineHeight(); // resets the line spacing
              break;
          case 'r':
              resetAll(); // resets everything
              break;
          default:
              break;
      }
  };

  window.addEventListener('keydown', handleKeyPress);

  return () => {
      window.removeEventListener('keydown', handleKeyPress);
  };
}, [fontSize]); 


  const resetLineHeight = () => {
    if (lineHeightCounter > 0) {
      setLineHeight(lineHeight=>lineHeight - 0.2);
      setLineHeightCounter(counter => counter - 1);
    }
  };

  //Reset
  const resetAll = () => {
    setFontSize(16);
    setFontSizeCounter(0);
    setLineHeight(1.5);
    setContrastMode(false);
    document.body.style.backgroundColor = '#ffffff';
    document.body.style.color = '#000000';
    const contrastableTextElements = document.querySelectorAll('.contrastable-text');
    contrastableTextElements.forEach(element => {
        element.style.color = ''; // Reset to default or your desired color
    });
  };

  return (
      <div className={`App ${contrastMode ? 'contrast-mode' : ''}`} style={{ fontSize: `${fontSize}px`, lineHeight: lineHeight }}>                    
                      
      <div className="top-right-buttons">             
      <a onClick={increaseFontSize}>
      <img className="top-image-button" src={aplus} alt="Button Schrift größer" title="Vergrößert die Schrift'+'" />
      </a>
      <a onClick={decreaseFontSize}>
        <img className="top-image-button" src={aminus} alt="Button Schrift kleiner" title="Verkleinert die Schrift'-'" />
      </a>
      <a onClick={toggleContrast}>
        <img className="top-image-button" src={bnw} alt="Button für Kontrast" title="Ändert den Kontrast'c'" />
      </a>
      <a onClick={resetContrast}>
        <img className="top-image-button" src={farbe} alt="Button für Kontrast zurücksetzen" title="Setzt den Kontrast zurück'd'" />
      </a>
      <a onClick={increaseLineHeight}>
        <img className="top-image-button" src={zplus} alt="Button für Zeileanbstand größer" title="Erhöht den Zeilenabstand'z'" />
      </a>
      <a onClick={resetLineHeight}>
        <img className="top-image-button" src={znormal} alt="Button für Zeilenabstand kleiner" title="Setzt den Zeilenabstand zurück't'" />
      </a>
      <a onClick={resetAll}>
        <img className="top-image-button" src={returnz} alt="Button für alles zurücksetzen" title="Setzt alles zurück'r'" />
      </a>
      <a onClick={() => { /* Aktion für Button 1 */ }}>
        <img className="top-image-button" src={sprache} alt="Button für Sprache ändern" title="Sprache ändern" />
      </a>

      
  </div>
   <div className={'logo-container'}>
   <img className={'project-logo'} src={logo} alt="Project Logo" style={{ maxWidth: '100%', height: 'auto' }} />   

      <a href="" target="_blank" rel="noopener noreferrer">
          <div className={'logo-container'}>
          <img className={'school-logo'} src={fhtwlogo} alt="FHTW Logo" style={{ maxWidth: '100%', height: 'auto' }} />
          </div>
        </a>
   </div>
   <div className="content-container" style={{ textAlign: 'center' }}>
                <h1 style={{ color: '#0a65c0' }}>Pathfinding for All - Enter Your Route and Explore FHTW</h1>
                <div>
                  <h1 style={{ color: '#4A4A4A' }}>{pathInfo}</h1>
                  <p>{pathDescription}</p>
                </div>
  </div>
      <div className={'button-container'}>
        <Link to="/">
          <button>Neue Suche</button>
        </Link>
      </div>
    </div>
    );
}
export default App2;
