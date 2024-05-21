import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Link, Routes } from 'react-router-dom'; 
import { useNavigate } from 'react-router-dom';
import Logo from './assets/Logo.jpg';
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

import './App.css';
import App2 from './App2.js';


function MainApp() {
  const backendUrl = process.env.REACT_APP_BACKEND_URL;
  console.log(process.env, 'ENV');
  const navigate = useNavigate();
  const [contrastMode, setContrastMode] = useState(false);
  const [fontSize, setFontSize] = useState(16); // Initial font size of 16px
  const [isParagraphLarge] = useState(false);
  const [lineHeight, setLineHeight] = useState(1.5); // Initial line height
  const [reset] = useState(1.5); // Initial line height
  const [fontSizeCounter, setFontSizeCounter] = useState(0);
  const [lineHeightCounter, setLineHeightCounter] = useState(0);
  const [startNode, setStartNode] = useState('');
  const [endNode, setEndNode] = useState('');
  const [isValidInput, setIsValidInput] = useState(false);

  const validNodes = ['F4', 'AUFZUG', 'TOILETTE', 'F4.27', 'F4.26', 'F4.25', 'F4.24', 'F4.23', 'F4.22', 'F4.20', 'F4.08', 'F4.07', 'F4.06', 'F4.05', 'F4.04', 'F4.03', 'F4.02', 'F4.01'];

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
  const resetLineHeight = () => {
    if (lineHeightCounter > 0) {
      setLineHeight(lineHeight => lineHeight - 0.2);
      setLineHeightCounter(counter => counter - 1);
  }
 };
  
 const handleKeyPress = (event) => {
  const key = event.key.toLowerCase(); // Get the pressed key in lowercase

  // Ignore the event if the target element is an input or textarea
  if (event.target.tagName === 'INPUT' || event.target.tagName === 'TEXTAREA') {
      return;
  }

  // Check if the key is a valid shortcut key and there are no modifier keys pressed
  if (!event.ctrlKey && !event.altKey && !event.shiftKey && !event.metaKey) {
      switch (key) {
          case '+':
              increaseFontSize(); // Increase the font size
              break;
          case '-':
              decreaseFontSize(); // Decrease the font size
              break;
          case 'c':
              toggleContrast(); // Toggle contrast mode
              break;
          case 'd':
              resetContrast(); // Reset contrast mode
              break;
          case 'z':
              increaseLineHeight(); // Increase line height
              break;
          case 't':
              resetLineHeight(); // Reset line height
              break;
          case 'r':
              resetAll(); // Reset all settings
              break;
          default:
              break;
      }
  }
};

// Attach the event listener for key presses
useEffect(() => {
  window.addEventListener('keydown', handleKeyPress);

  // Clean up by removing the event listener when component unmounts
  return () => {
      window.removeEventListener('keydown', handleKeyPress);
  };
}, [fontSize, lineHeight]); // Re-run effect when fontSize or lineHeight change

    const handleFindPath = async () => {
        console.log("start: ", startNode);
        console.log("end: ", endNode);

        try {
            const response = await fetch(`${backendUrl}/fhtways/find-path/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ startNode, endNode }),
            });
    
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
    
            const data = await response.json();
            navigate('/app2', { state: { startNode, endNode, pathDescription: data.path } }); 

          } catch (error) {
            console.error('Error fetching path data:', error);
        }       
  };

 // Focus management: Set initial focus to the start input field
 useEffect(() => {
  const startInput = document.getElementById('startInput');
  if (startInput) {
    startInput.focus();
  }
}, []);


 //input
 const handleStartNodeChange = (e) => {
  const input = e.target.value;
  const formattedInput = formatRoomNumber(input);
  setStartNode(formattedInput);
  validateInput(formattedInput, endNode);
};

const handleEndNodeChange = (e) => {
  const input = e.target.value;
  const formattedInput = formatRoomNumber(input);
  setEndNode(formattedInput);
  validateInput(startNode, formattedInput);
};

const formatRoomNumber = (input) => {
  // Regular expression to match room number formats: building + floor + room
  const validFormatRegex = /^([A-Z])(\d+)(?:\.(\d+))?$/i;

  // Check if the input matches the valid format
  const match = input.trim().toUpperCase().match(validFormatRegex);

  if (!match) {
      // If no match, attempt to parse the input more flexibly
      const cleanedInput = input.replace(/[^A-Z0-9]/ig, ''); // Remove non-alphanumeric characters
      const building = cleanedInput.match(/[A-Z]/i)?.[0] || ''; // Extract building (first letter)
      const numbers = cleanedInput.match(/\d+/g); // Extract all numeric sequences

      if (building && numbers) {
          const floor = numbers[0];
          const room = numbers[1] || '';

          if (room) {
              // Return formatted room number (building + floor + room)
              return `${building}${floor}.${room}`;
          } else {
              // Return formatted floor number only (building + floor)
              return `${building}${floor}`;
          }
      }

      return input; // Return input as-is if unable to parse
  }

  // Extract building, floor, and room number from the matched groups
  const [, building, floor, room] = match;

  if (room) {
      // If the room number is already in the correct format (e.g., F4.24), return it unchanged
      return `${building}${floor}.${room}`;
  } else {
      // If the room number is in simplified format (e.g., F424), format it as F4.24
      const roomInfo = floor; // Use 'floor' as the roomInfo
      if (roomInfo.length === 3) {
          // If roomInfo has length 3 (e.g., "424"), assume the first character is the floor
          const floorNumber = roomInfo.charAt(0);
          const roomNumber = roomInfo.substring(1);
          return `${building}${floorNumber}.${roomNumber}`;
      } else if (roomInfo.length === 4) {
          // If roomInfo has length 4 (e.g., "0424"), the first two characters are considered the floor
          const floorNumber = roomInfo.substring(0, 2);
          const roomNumber = roomInfo.substring(2);
          return `${building}${floorNumber}.${roomNumber}`;
      } else {
          return input; // Return input as-is if the roomInfo length is unexpected
      }
  }
};

  const [errorMessage, setErrorMessage] = useState('');

 
  const validateInput = (start, end) => {
    const isValidFormat = /^(AUFZUG|TOILETTE|[A-Z]\d+(\.\d+)?)$/i.test(start) && /^(AUFZUG|TOILETTE|[A-Z]\d+(\.\d+)?)$/i.test(end);
    const isValid = validNodes.includes(start) && validNodes.includes(end) && isValidFormat;
  
    setIsValidInput(isValid);
  
    // Set error message for invalid format
    if (start.trim() === '' || end.trim() === '') {
      setErrorMessage('Bitte geben Sie sowohl die Anfangs- als auch die Endraumnummer ein.');
    } else if (!isValidFormat) {
      setErrorMessage('Ungültiges Eingabeformat! Bitte geben Sie die Zimmernummer im richtigen Format ein.');
    } else if (!isValid) {
      setErrorMessage(`Ungültige Eingabe! Bitte geben Sie gültige Zimmernummern ein. Zulässige Zimmernummern sind: ${validNodes.join(', ')}`);
    } else {
      setErrorMessage(''); // Clear error message if input is valid
    }
  };

//Reset
  const resetAll = () => {
    setIsValidInput(true); // Reset input validity when resetting
    setStartNode('');
    setEndNode('');
    setFontSize(16);
    setFontSizeCounter(0);
    setLineHeight(1.5);
    setContrastMode(false);
    document.body.style.backgroundColor = '#ffffff';
    document.body.style.color = '#000000';
     // Clear the input fields
    const startInput = document.getElementById('startInput');
    const endInput = document.getElementById('endInput');
    if (startInput && endInput) {
      startInput.value = '';
      endInput.value = '';
    }
    const contrastableTextElements = document.querySelectorAll('.contrastable-text');
    contrastableTextElements.forEach(element => {
        element.style.color = ''; // Reset to default or your desired color
    });
  };
    return (
            <div className={`App ${contrastMode ? 'contrast-mode' : ''}`} style={{ fontSize: `${fontSize}px`, lineHeight: lineHeight }}>                    
                    
                <div className="top-right-buttons">             
                <a href="#" onClick={increaseFontSize}>
                  <img className="top-image-button" src={aplus} alt="Button Schrift größer" title="Vergrößert die Schrift'+'" />
                </a>
                <a href="#" onClick={decreaseFontSize}>
                  <img className="top-image-button" src={aminus} alt="Button Schrift kleiner" title="Verkleinert die Schrift'-'" />
                </a>
                <a href="#" onClick={toggleContrast}>
                  <img className="top-image-button" src={bnw} alt="Button für Kontrast" title="Ändert den Kontrast'c'" />
                </a>
                <a href="#" onClick={resetContrast}>
                  <img className="top-image-button" src={farbe} alt="Button für Kontrast zurücksetzen" title="Setzt den Kontrast zurück'd'" />
                </a>
                <a href="#" onClick={increaseLineHeight}>
                  <img className="top-image-button" src={zplus} alt="Button für Zeileanbstand größer" title="Erhöht den Zeilenabstand'z'" />
                </a>
                <a href="#" onClick={resetLineHeight}>
                  <img className="top-image-button" src={znormal} alt="Button für Zeilenabstand kleiner" title="Setzt den Zeilenabstand zurück't'" />
                </a>
                <a href="#" onClick={resetAll}>
                  <img className="top-image-button" src={returnz} alt="Button für alles zurücksetzen" title="Setzt alles zurück'r'" />
                </a>
                <a href="#" onClick={() => { /* Aktion für Button 1 */ }}>
                  <img className="top-image-button" src={sprache} alt="Button für Sprache ändern" title="Sprache ändern" />
                </a>

                
            </div>
            <div className={'logo-container'}>
                
            <img className={'project-logo'} src={Logo} alt="Project Logo" />

                <a href="" target="_blank" rel="noopener noreferrer">
                <div className={'logo-container'}>
                    <img className={'school-logo'} src={fhtwlogo} alt="FHTW Logo" />
                </div>
                </a>
            </div>
            
            <div>
                <div className="content-container" style={{ textAlign: 'center', fontSize: `${fontSize}px` }}>
                <h1 lang="en" style={{ color: '#0a65c0' }}>Pathfinding for All - Enter Your Route and Explore FHTW</h1>
                </div>
                
                <div className="content-container"style={{ fontSize: `${fontSize}px` }}>        
                <p className="contrastable-text"  style={{ fontSize: isParagraphLarge ? '24px' : 'inherit'}}>
                        Mit FHTWays können Sie durch die FHTW navigieren! Geben Sie Ihren Startpunkt und Ihr Ziel in das vorgesehene Format ein:
                    [Gebäude][Stockwerk]'Punkt'[Raum]. Beispiel: F4.24 für Gebäude F, 4. Stockwerk, Raum 24. Klicken Sie auf den
                    "Los"-Button oder drücken Sie die Enter-Taste, um Ihre Routenanfrage zu starten und folgen Sie den detaillierten
                    Wegbeschreibungen!</p>
                    
                <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', marginTop: '20px' }}>
                  <div style={{ display: 'grid', gridTemplateColumns: 'auto 1fr auto', alignItems: 'center', columnGap: '10px', marginBottom: '5px' }}>
                    <p className="contrastable-text" style={{ fontWeight: 'bolder', margin: '0', fontSize: '32px' }}>Start</p>
                    <div style={{ display: 'flex', alignItems: 'center'}}>
                      <div className={'search-bar-start'} style={{ width: '100%', marginBottom: '10px' }}>
                            <input
                                id="startInput"
                                type="text"
                                value={startNode}
                                pattern="[A-Z]\d+(\.\d+)?"
                                placeholder="Geben Sie Ihren Startpunkt an..."
                                style={{ width: '100%', backgroundColor: startNode ? '#cfe3fa' : '#ffffff'}}
                                onChange={handleStartNodeChange}
      
                            />
                            </div>
                        </div>
                        <div style={{ width: '20px' }}></div>
                        </div>

                        <div style={{ display: 'grid', gridTemplateColumns: 'auto 1fr auto', alignItems: 'center', columnGap: '10px',  marginBottom: '5px' }}>
                          <p className="contrastable-text" style={{ fontWeight: 'bold', margin: '0', fontSize: '32px' }}>Ziel</p>
                          <div style={{ display: 'flex', alignItems: 'center', marginLeft: '-5px' }}>
                            <div className={'search-bar-end'} style={{ width: '100%', marginBottom: '10px' }}>
                            <input
                                id="endInput"
                                type="text"
                                value={endNode}
                                pattern="[A-Z]\d+(\.\d+)?"
                                placeholder="Geben Sie Ihren Endpunkt an..."
                                style={{ width: '100%', backgroundColor: endNode ? '#cfe3fa' : '#ffffff'}}
                                onChange={handleEndNodeChange}
                            />
                            </div>
                        </div>
                        <div style={{ width: '20px' }}></div>
                        </div>
                </div>
                <div className={'button-container'}>
                  <button 
                      disabled={!isValidInput} 
                      onClick={isValidInput ? handleFindPath : () => alert(errorMessage)} 
                      style={{
                          backgroundColor: isValidInput ? '#0a65c0' : '#CCCCCC', 
                          cursor: isValidInput ? 'pointer' : 'not-allowed'
                      }}>                           
                      Los!
                  </button>
                </div>
                    {!isValidInput && (
                        <p  style={{ color: 'red', fontSize: '20px', textAlign: 'center' }}>
                        {errorMessage}
                      </p>
                    )}
                    <p className="contrastable-text" style={{ fontSize: isParagraphLarge ? '24px' : 'inherit'}}> *mit "TOILETTE" und "AUFZUG" können Sie direkt zu den nächstliegenden Herren-, Damen-, Diverstoiletten bzw. Aufzügen navigieren</p>
                    <p className="contrastable-text" style={{ fontSize: isParagraphLarge ? '24px' : 'inherit'}}> *für den Eingang ins Gebäude bzw. in den Stockwerk verwenden Sie einfach die Buchstabe des jeweiligen Gebäudes bzw. Stockwerkes, z.B. F4 für den Stockwerk</p>
                    <p className="contrastable-text" style={{ fontSize: isParagraphLarge ? '24px' : 'inherit'}}>Barrierefreiheit-Tastenkombinationen: '+' Vergrößert die Schrift.   '-' Verkleinert die Schrift.   'c' Ändert den Kontrast.   'd' Setzt den Kontrast zurück.   'z' Erhöht den Zeilenabstand.   't' Setzt den Zeilenabstand zurück.   'r' Setzt alles zurück.</p>
                    

                </div>
            </div>
          
        </div>
    );
  }

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<MainApp />} />
                <Route path="/app2" element={<App2 />} />
            </Routes>
        </Router>
    );
}
export default App;
