import { useState, useEffect} from "react";
import { BrowserRouter } from "react-router-dom";
import { About, Contact, Experience, Feedbacks, Hero, Navbar, Tech, Works, StarsCanvas } from "./components";

const App = () => {
  const getCurrentTheme = () => {
    const currentHour = new Date().getHours();
    if (currentHour >= 5 && currentHour < 12) return "morning-theme";
    if (currentHour >= 12 && currentHour < 17) return "afternoon-theme";
    if (currentHour >= 17 && currentHour < 21) return "evening-theme";
    return "night-theme";
  };

  const [currentTheme, setCurrentTheme] = useState(getCurrentTheme());


  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentTheme(getCurrentTheme());
    }, 60000); // Update every minute

    return () => clearInterval(interval);
  }, []);

  return (
    <BrowserRouter>
      <div className={`relative z-0 ${currentTheme}`}>
        <div className="bg-hero-pattern bg-cover bg-no-repeat bg-center">
          <Navbar />
          <Hero />
        </div>
        <About />
        <Experience />
        <Tech />
        <Works />
        <Feedbacks />
        <div className="relative z-0">
          <Contact />
          <StarsCanvas />
        </div>
      </div>
      <div className="container">
        <div className="chatbot-popup">

          <div className="chat-header">
            <div className="header-info">
              <h2></h2>
            </div>
            <button class="material-symbols-outlined">keyboard_arrow_down</button>
          </div>

          <div className="chat-body">
            <div className="message bot-message">
              Hey there 
            </div>

          </div>
  
        </div>
      </div>

      
    </BrowserRouter>
    
  );
};

export default App;