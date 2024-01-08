import React, { useState } from 'react';
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
import Moodle from  './assets/icons/moodle.png';
import Cis from  './assets/icons/cis.png';
import Linkedin from  './assets/icons/linkedin.png';
import Email from  './assets/icons/mail.png';
import { Link } from 'react-router-dom';


function App2(){
    const location = useLocation();
    const pathDescription = location.state?.pathDescription || 'No path description available';
    console.log("Path Description in App2:", pathDescription); // Log the path description
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
  return (
                <div className={`App2 ${contrastMode ? 'contrast-mode' : ''}`} style={{ fontSize: `${fontSize}px`, lineHeight: lineHeight }}>                <div className="top-right-buttons">             

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
   <img className={'project-logo'} src={logo} alt="Project Logo" />

       <a href="https://www.technikum-wien.at/" target="_blank" rel="noopener noreferrer">
       <div className={'logo-container'}>
           <img className={'school-logo'} src={fhtwlogo} alt="FHTW Logo" />
       </div>
       </a>
   </div>
   <div className="content-container" style={{ textAlign: 'center' }}>
                <h1 style={{ color: '#0a65c0' }}>Pathfinding for All - Enter Your Route and Explore FHTW</h1>
                <div>
                  <h1>Path Description</h1>
                  <p>{pathDescription}</p>
                </div>
  </div>
  <div className={'button-container'}>
    <Link to="/">
    <button>Neue Suche</button>
    </Link>
  </div>
   <nav className={'footer-nav'} style={{ textAlign: 'center', bottom: 0}}>
                 <ul style={{ listStyle: 'none', padding: 0 }}>
                <li><Link to="/">Startseite</Link></li>
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
export default App2;
