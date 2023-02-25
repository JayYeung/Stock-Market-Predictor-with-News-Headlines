import Head from 'next/head'
import Image from 'next/image'
import { Inter } from '@next/font/google'
import React, { Component, useState, useEffect, CSSProperties} from 'react';
import { Navbar, Nav } from 'react-bootstrap';
import { FaPython, FaReact, FaFlask, FaGitAlt, FaJsSquare} from 'react-icons/fa';
import { FaFileCode, FaJava, FaCode, FaHtml5, FaCss3Alt, FaGithub, FaYoutube } from 'react-icons/fa';
import { FaEnvelope, FaPhone, FaDiscord, FaSpotify, FaGamepad } from 'react-icons/fa';
import { SiLeetcode } from 'react-icons/si';
import { AiFillGoogleCircle } from 'react-icons/ai';
import 'bootstrap/dist/css/bootstrap.min.css';

const inter = Inter({ subsets: ['latin'] });
const headingStyles: CSSProperties = {
  fontSize: "2rem",
  fontWeight: "bold",
  marginTop: "2rem",
  marginBottom: "1rem",
  color: "orange",
};

function NavigationBar() {
  const [scrollPos, setScrollPos] = useState(0);
  const [navbarClass, setNavbarClass] = useState('');

  useEffect(() => {
    function handleScroll() {
      setScrollPos(document.body.getBoundingClientRect().top);
    }

    window.addEventListener('scroll', handleScroll);
    return () => {
      window.removeEventListener('scroll', handleScroll);
    };
  }, []);

  useEffect(() => {
    if (scrollPos < -200) { // adjust this value to determine when the navbar appears
      setNavbarClass('fixed-top');
    } else {
      setNavbarClass('');
    }
  }, [scrollPos]);

  return (
    <Navbar bg="dark" variant="dark" expand="lg" className={navbarClass}>
      <Navbar.Toggle aria-controls="basic-navbar-nav" />
      <Navbar.Collapse id="basic-navbar-nav">
        <Nav className="mr-auto">
          <Nav.Link href="#about">About</Nav.Link>
          <Nav.Link href="#skills">Skills</Nav.Link>
          <Nav.Link href="#projects">Projects</Nav.Link>
          <Nav.Link href="#contact">Contact</Nav.Link>
        </Nav>
        <Navbar.Brand href="/Jay Yeung Technical Resume.pdf" className="ml-auto rounded-lg hover:bg-orange-600 transition-colors duration-1000">
          Resume
        </Navbar.Brand>
      </Navbar.Collapse>
    </Navbar>
  );
}

function About() {
  return (
    <div>
      <div className="dark">
        <h1 className="text-white text-center text-6xl">
         👋 Hi, I'm Jay Yeung!
        </h1>
      </div>
      <div className="container mx-auto mt-8" id="about">
        <h2 style={headingStyles}>About Me</h2>
        <p>
          <em className="text-white">
            I'm an aspiring Computer Science and Data Science major.
          </em>
        </p>
      </div>
    </div>
  );
}




function Skills() {
  return (
    <div className="container mx-auto mt-8" id="skills">
      <h1 style={headingStyles}>My Skills</h1>
      <div className="container mx-auto mt-8">
        <h2 className="text-white text-xl font-bold">Programming Languages:</h2>
        <ul className="list-none text-white flex flex-wrap">
          <li className="flex items-center mr-4 mb-4"><FaFileCode className="mr-2" /> C++</li>
          <li className="flex items-center mr-4 mb-4"><FaJava className="mr-2" /> Java</li>
          <li className="flex items-center mr-4 mb-4"><FaPython className="mr-2" /> Python</li>
          <li className="flex items-center mr-4 mb-4"><FaCode className="mr-2" /> Perl</li>
          <li className="flex items-center mr-4 mb-4"><FaHtml5 className="mr-2" /> HTML</li>
          <li className="flex items-center mr-4 mb-4"><FaCss3Alt className="mr-2" /> CSS</li>
          <li className="flex items-center mr-4 mb-4"><FaJsSquare className="mr-2" /> JavaScript</li>
        </ul>
        <h2 className="text-white text-xl font-bold mt-8">Frameworks and Libraries:</h2>
        <ul className="list-none text-white flex flex-wrap">
          <li className="flex items-center mr-4 mb-4"><FaPython className="mr-2" /> NumPy</li>
          <li className="flex items-center mr-4 mb-4"><FaPython className="mr-2" /> Pandas</li>
          <li className="flex items-center mr-4 mb-4"><FaPython className="mr-2" /> SciPy</li>
          <li className="flex items-center mr-4 mb-4"><FaPython className="mr-2" /> Matplotlib</li>
          <li className="flex items-center mr-4 mb-4"><FaPython className="mr-2" /> Scikit-learn (Sk-Learn)</li>
          <li className="flex items-center mr-4 mb-4"><FaFlask className="mr-2" /> Flask</li>
          <li className="flex items-center mr-4 mb-4"><FaGitAlt className="mr-2" /> Git</li>
          <li className="flex items-center mr-4 mb-4"><FaReact className="mr-2" /> React</li>
        </ul>
      </div>
    </div>
  );
}

interface ProjectProps {
  title: string;
  description: string;
  imageUrl: string;
  githubLink: string;
  youtubeLink?: string;
  colabLink?: string;
}

function Project(props: ProjectProps) {
  return (
    <div className="project mx-auto mt-8">
      <div className="project-info text-white">
        <h3>{props.title}</h3>
        <img src={props.imageUrl} alt={props.title} />
        <div className="project-links">
          {props.githubLink && (
            <a
              href={props.githubLink}
              target="_blank"
              rel="noopener noreferrer"
              className="text-white inline-block mt-4 mr-4 px-4 py-2 rounded-lg bg-blue-900 hover:bg-blue-600 transition-colors duration-300"
            >
              <FaGithub className="inline-block mr-2 text-white" />
              GitHub
            </a>
          )}
          {props.youtubeLink && (
            <a
              href={props.youtubeLink}
              target="_blank"
              rel="noopener noreferrer"
              className="text-white inline-block mt-4 mr-4 px-4 py-2 rounded-lg bg-red-900 hover:bg-red-600 transition-colors duration-300"
            >
              <FaYoutube className="inline-block mr-2 text-white" />
              YouTube Demo
            </a>
          )}
          {props.colabLink && (
            <a
              href={props.colabLink}
              target="_blank"
              rel="noopener noreferrer"
              className="text-white inline-block mt-4 px-4 py-2 rounded-lg bg-yellow-900 hover:bg-yellow-600 transition-colors duration-300"
            >
              <AiFillGoogleCircle className="inline-block mr-2 text-white" />
              Google Colab
            </a>
          )}
        </div>
        <p>{props.description}</p>
      </div>
    </div>
  );
}


function Projects() {
  return (
    <div className="container mx-auto mt-8" id="projects">
      <h2 style={headingStyles}>My Projects</h2>
      <div className="grid grid-cols-3 gap-8">
        <Project
          title="Stock Market Predictor with News Headlines"
          imageUrl="/project1.png"
          description="Created a robot that consumes news headlines and historical performance data and predicts the stock market trend with 80% accuracy."
          githubLink="https://github.com/JayYeung/Stock-Market-Predictor-with-News-Headlines"
          colabLink="https://colab.research.google.com/drive/16B1JqUOd8ZUQrqnJOqQr-U8LkaADcR5D#scrollTo=00NgQFkWRz4g"
        />
        <Project
          title="VLSI Place & Route tool using Kernighan-Lin algorithm"
          imageUrl="/project2.png"
          description="Developed a C++ based VLSI Place & Route tool by using the Kernighan-Lin algorithm to optimize the data structures being used and speed up the run time from 50 to 4500 gates in seven hours."
          githubLink="https://github.com/JayYeung/VLSI-Place-Route-tool-using-Kernighan-Lin-algorithm"
        />
        <Project
          title="Auto Annotater and Summarizer"
          imageUrl="/project3.gif"
          description="Created a robot that automatically annotates and/or summarizes an online assignment"
          githubLink="https://github.com/JayYeung/auto-annotater-and-summarizer"
          youtubeLink="https://youtu.be/YDGyyvQ9aDs"
        />
        <Project
          title="Disaster Relief"
          imageUrl="/project7.png"
          description="Developed a machine learning and natural language processing (NLP) program that efficiently categorizes tweets into relevant topics such as food, energy, and water. "
          githubLink="https://github.com/JayYeung/Disaster-Relief-Inspirit-AI-Project"
          youtubeLink="https://www.youtube.com/watch?v=bTDPc5uDzNc"
        />
        <Project
          title="Binary-to-ATE"
          imageUrl="/project6.png"
          description="Created a Perl program to convert firmware code from binary to ATE (automatic test equipment) code format to streamline test code loading flow"
          githubLink="https://github.com/JayYeung/Binary-to-ATE"
        />
        <Project
          title="Auto Grader for Online Assignments"
          imageUrl="/project4.gif"
          description="Created a bot that grades a large number of assignments at once."
          githubLink="https://github.com/JayYeung/auto-grader"
          youtubeLink="https://youtu.be/Y3qmQAJ0S58"
        />
        <Project
        title="Kindling (online dating app)"
        imageUrl="/project5.png"
        description="Kindling is an online dating app that allows users to practice online dating without knowing the race of their partners"
        githubLink="https://github.com/JayYeung/Kindling"
        youtubeLink="https://youtu.be/zVkgrkei52o"
        />

      </div>
    </div>
  );
}

function Contact() {
  const linkStyle = {
    display: 'flex',
    margin: '0.5rem 0',
    color: 'white',
  };

  return (
    <div>
      <div className="container mx-auto mt-8" id="contact">
        <h2 style={headingStyles}>Contact Me</h2>
        <div style={linkStyle}>
          <FaEnvelope size={20} style={{ marginRight: '0.5rem' }} />
          <a href="mailto:JayYeungScout@gmail.com">JayYeungScout@gmail.com</a>
        </div>
        <div style={linkStyle}>
          <FaPhone size={20} style={{ marginRight: '0.5rem' }} />
          <span>1 (650) 293-7697</span>
        </div>
        <div style={linkStyle}>
          <FaGithub size={20} style={{ marginRight: '0.5rem' }} />
          <a href="https://github.com/JayYeung">Github Repo</a>
        </div>
        <div style={linkStyle}>
          <FaDiscord size={20} style={{ marginRight: '0.5rem' }} />
          <span>JayBoi#0403</span>
        </div>
        <div style={linkStyle}>
          <SiLeetcode size={20} style={{ marginRight: '0.5rem' }} />
          <a href="https://leetcode.com/rukt/">LeetCode Profile</a>
        </div>
        <div style={linkStyle}>
          <FaSpotify size={20} style={{ marginRight: '0.5rem' }} />
          <a href="https://open.spotify.com/user/31iydromoa3hmngys4azauubcbxu">Spotify</a>
        </div>
        <div style={linkStyle}>
          <FaGamepad size={20} style={{ marginRight: '0.5rem' }} />
          <span>"Rukt" on Val and MC</span>
        </div>
      </div>
    </div>
  );
}


export default function Home() {
  return (
    <>
      <Head>
        <title>Hi, I'm Jay Yeung!</title>
        <meta name="description" content="Software engineer with experience in data science and a fun-loving personality" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <div className='bg-black'>
        {/* NAVBAR */}
        <NavigationBar />

        {/* ABOUT ME */}
        <About />

        {/* Skills */}
        <Skills />

        {/* Projects */}
        <Projects />

        {/* Contact Me */}
        <Contact />
      </div>
    </>
  )
}
