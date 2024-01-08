import React, { useState } from 'react';
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
import Moodle from  './assets/icons/moodle.png';
import Cis from  './assets/icons/cis.png';
import Linkedin from  './assets/icons/linkedin.png';
import Email from  './assets/icons/mail.png';

import './App.css';
import App2 from './App2.js';


function MainApp() {
    const [start, setStart] = useState('');
    const [end, setEnd] = useState('');
    const navigate = useNavigate();
    
    const [contrastMode, setContrastMode] = useState(false);
    const [fontSize, setFontSize] = useState(16); // Initial font size of 16px
    const [isParagraphLarge, setIsParagraphLarge] = useState(false);
    const [lineHeight, setLineHeight] = useState(1.5); // Initial line height
    const [reset] = useState(1.5); // Initial line height
    const toggleContrast = () => {
    setContrastMode(!contrastMode);
    // Logic to change contrast mode and colors accordingly
    if (!contrastMode) {
      document.body.style.backgroundColor = '#000000';
      document.body.style.color = '#ffffff';
    } else {
      document.body.style.backgroundColor = '#ffffff';
      document.body.style.color = '#000000';
    }
  };

    const resetContrast = () => {
        setContrastMode(false);
        document.body.style.backgroundColor = '#ffffff';
        document.body.style.color = '#000000';
    };

    const increaseFontSize = () => {
        setFontSize(fontSize + 4); // Schriftgröße um 4 Pixel erhöhen
        setIsParagraphLarge(true); // Setze den Zustand für den vergrößerten Absatz auf true
    };

    const resetFontSize = () => {
        setFontSize(16); // Schriftgröße auf 16 Pixel zurücksetzen
        setIsParagraphLarge(false); // Setze den Zustand für den vergrößerten Absatz auf false
    };
    const increaseLineHeight = () => {
        setLineHeight(lineHeight + 0.2); // Zeilenabstand um 0.2 erhöhen
    };

    const resetLineHeight = () => {
        setLineHeight(1.5); // Zeilenabstand zurücksetzen
    };

    const resetAll = () => {
        setFontSize(16);
        setLineHeight(1.5);
        setContrastMode(false);
        document.body.style.backgroundColor = '#ffffff';
        document.body.style.color = '#000000';
    };

    const handleFindPath = async () => {
        console.log("start: ", start);
        console.log("end: ", end);

        try {
            const response = await fetch('http://localhost:8000/fhtways/find-path/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ start, end }),
            });
    
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
    
            const data = await response.json();
            navigate('/app2', { state: { pathDescription: data.path } });
    
        } catch (error) {
            console.error('Error fetching path data:', error);
        }
    };

    return (
        <div className={`App ${contrastMode ? 'contrast-mode' : ''}`} style={{ fontSize: `${fontSize}px`, lineHeight: lineHeight }}>                <div className="top-right-buttons">             
                <a href="#" onClick={() => { /* Action for Button 1 */ }}>
                    <img className="top-image-button" src={adiobook} alt="Button 1" />
                </a>
                
                <a href="#" onClick={increaseFontSize}><img className="top-image-button" src={aplus} alt="Button 2" /></a>
                <a href="#" onClick={resetFontSize}><img className="top-image-button" src={aminus} alt="Button 3" /></a>

                <a href="#" onClick={toggleContrast}><img className="top-image-button" src={bnw} alt="Button 4" /></a>
                <a href="#" onClick={resetContrast}><img className="top-image-button" src={farbe} alt="Button 5" /></a>
               
                <a href="#" onClick={increaseLineHeight}><img className="top-image-button" src={zplus} alt="Button 6" /></a>
                <a href="#" onClick={resetLineHeight}><img className="top-image-button" src={znormal} alt="Button 7" /></a>
               
                <a href="#" onClick={resetAll}><img className="top-image-button" src={returnz} alt="Button 8" /></a>
                <a href="#" onClick={() => { /* Action for Button 1 */ }}>
                    <img className="top-image-button" src={sprache} alt="Button 1" />
                </a>
                
            </div>
            <div className={'logo-container'}>
            <img className={'project-logo'} src={Logo} alt="Project Logo" />

                <a href="https://www.technikum-wien.at/" target="_blank" rel="noopener noreferrer">
                <div className={'logo-container'}>
                    <img className={'school-logo'} src={fhtwlogo} alt="FHTW Logo" />
                </div>
                </a>
            </div>
            
            
           
            <div>
            <div className="content-container" style={{ textAlign: 'center' }}>
                <h1 style={{ color: '#0a65c0' }}>Pathfinding for All - Enter Your Route and Explore FHTW</h1>
                </div>
                
                <div className="content-container"style={{ fontSize: `${fontSize}px` }}>        
                    <p style={{ fontSize: isParagraphLarge ? '24px' : 'inherit'}}>
                        Mit FHTWays können Sie durch die FHTW navigieren! Geben Sie Ihren Startpunkt und Ihr Ziel in das vorgesehene Format ein:
                    [Gebäude][Stockwerk]'Punkt'[Raum]. Beispiel: F4.24 für Gebäude F, 4. Stockwerk, Raum 24. Klicken Sie auf den
                    "Los"-Button oder drücken Sie die Enter-Taste, um Ihre Routenanfrage zu starten und folgen Sie den detaillierten
                    Wegbeschreibungen!</p>
                    
                <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', marginTop: '20px' }}>
                    <div style={{ display: 'grid', gridTemplateColumns: 'auto 1fr auto', alignItems: 'center', columnGap: '10px', marginBottom: '5px' }}>
                        <p style={{ fontWeight: 'bolder', margin: '0', fontSize: '32px' }}>Start</p>
                        <div style={{ display: 'flex', alignItems: 'center', marginLeft: '-5px' }}>
                            <div className={'search-bar'} style={{ width: '100%' }}>
                                <input
                                    type="text"
                                    placeholder="Geben Sie Ihren Startpunkt an..."
                                    value={start}
                                    onChange={(e) => setStart(e.target.value)}
                                    style={{ width: '100%' }}
                                />
                            </div>
                        </div>
                        <div style={{ width: '20px' }}></div>
                    </div>
                    <div style={{ display: 'grid', gridTemplateColumns: 'auto 1fr auto', alignItems: 'center', columnGap: '10px', marginBottom: '5px' }}>
                        <p style={{ fontWeight: 'bold', margin: '0', fontSize: '32px'}}>Ziel</p>
                        <div style={{ display: 'flex', alignItems: 'center', marginLeft: '-5px' }}>
                            <div className={'search-bar'} style={{ width: '100%' }}>
                                <input
                                    type="text"
                                    placeholder="Geben Sie Ihr Ziel an..."
                                    value={end}
                                    onChange={(e) => setEnd(e.target.value)}
                                    style={{ width: '100%' }}
                                />
                            </div>
                        </div>
                        <div style={{ width: '20px' }}></div>
                    </div>
                </div>

                     <div className={'button-container'}>
                        <button onClick={handleFindPath}>Los!</button>
                     </div>
                    <p style={{ fontSize: isParagraphLarge ? '24px' : 'inherit'}}> *mit den Buchstaben "M", "W" oder “D” im [Zimmer] können Sie direkt zu den nächstliegenden Herren-, Damen-, Diverstoiletten navigieren</p>
                    <p style={{ fontSize: isParagraphLarge ? '24px' : 'inherit'}}> *für den Eingang ins Gebäude verwenden Sie einfach die Buchstabe des jeweiligen Gebäudes, z.B. F für das Gebäude </p>
                </div>
            </div>
            <nav className={'footer-nav'} style={{ textAlign: 'center'}}>
                 <ul style={{ listStyle: 'none', padding: 0 }}>
                <li>Startseite</li>
                <li>Impressum</li>
                <li>Kontakt</li>
                <li>Über uns</li>
                </ul>
                <ul style={{ listStyle: 'none', padding: 0, display: 'flex', justifyContent: 'center' }}>
                <li>
                    <a href="https://moodle.technikum-wien.at/" target="_blank" rel="noopener noreferrer">
                    <img className="top-image-button" src={Moodle} alt="Moodle" />
                    </a>
                </li>
                <li>
                    <a href="https://cis.technikum-wien.at/cis/index.html" target="_blank" rel="noopener noreferrer">
                    <img className="top-image-button" src={Cis} alt="Cis" />
                    </a>
                </li>
                <li>
                    <a href="https://www.linkedin.com/school/uas-technikum-wien/?originalSubdomain=at" target="_blank" rel="noopener noreferrer">
                    <img className="top-image-button" src={Linkedin} alt="Linkedin" />
                    </a>
                </li>
                <li>
                    <a href="https://sogo.technikum-wien.at/SOGo/">
                    <img className="top-image-button" src={Email} alt="Email" />
                    </a>
                </li>
        </ul>
             <p style={{ fontSize: '15px', color: 'white', fontWeight: 'bold' }}>© Copyright 2023 - FHTWays</p>
            </nav>
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
