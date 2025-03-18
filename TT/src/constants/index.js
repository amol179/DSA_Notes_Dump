import {
  mobile,
  backend,
  creator,
  web,
  javascript,
  typescript,
  html,
  css,
  reactjs,
  redux,
  tailwind,
  nodejs,
  mongodb,
  git,
  figma,
  docker,
  meta,
  starbucks,
  tesla,
  shopify,
  carrent,
  jobit,
  tripguide,
  threejs,
} from "../assets";

export const navLinks = [
  {
    id: "about",
    title: "About",
  },
  {
    id: "work",
    title: "Events",
  },
  {
    id: "contact",
    title: "Contact",
  },
];

const services = [
  {
    title: "Web Developer",
    icon: web,
  },
  {
    title: "React Native Developer",
    icon: mobile,
  },
  {
    title: "Backend Developer",
    icon: backend,
  },
  {
    title: "Content Creator",
    icon: creator,
  },
];

const technologies = [
  {
    name: "HTML 5",
    icon: html,
  },
  {
    name: "CSS 3",
    icon: css,
  },
  {
    name: "JavaScript",
    icon: javascript,
  },
  {
    name: "TypeScript",
    icon: typescript,
  },
  {
    name: "React JS",
    icon: reactjs,
  },
  {
    name: "Redux Toolkit",
    icon: redux,
  },
  {
    name: "Tailwind CSS",
    icon: tailwind,
  },
  {
    name: "Node JS",
    icon: nodejs,
  },
  {
    name: "MongoDB",
    icon: mongodb,
  },
  {
    name: "Three JS",
    icon: threejs,
  },
  {
    name: "git",
    icon: git,
  },
  {
    name: "figma",
    icon: figma,
  },
  {
    name: "docker",
    icon: docker,
  },
];

const experiences = [
  {
    title: "Registration & AI Welcome",
    company_name: "Registration & AI Welcome",
    icon: starbucks,
    iconBg: "#383E56",
    date: "9:00 AM",
    points: [
      "Start your day by checking in. Our smart AI concierge will greet you and guide you through the event.",
    ],
  },
  {
    title: "Futuristic Keynote Speech",
    company_name: "Futuristic Keynote Speech",
    icon: tesla,
    iconBg: "#E6DEDD",
    date: "10:00 AM ",
    points: [
      "Listen to our main speaker explain how new technologies like AI and robotics are shaping our future in easy-to-understand language.",
    ],
  },
  {
    title: "Interactive 3D Tech Demo",
    company_name: "Interactive 3D Tech Demo ",
    icon: shopify,
    iconBg: "#383E56",
    date: "11:00 AM  ",
    points: [
      "Explore interactive 3D models that show you how futuristic technology works in a fun and engaging way.",
    ],
  },
  {
    title: "Guest Speaker Session",
    company_name: "Guest Speaker Session",
    icon: meta,
    iconBg: "#E6DEDD",
    date: "12:00 PM",
    points: [
      "Join industry experts as they share practical insights about modern innovations and explain how technology impacts our daily lives.",
    ],
  },
  {
    title: "Live AI Chat Support Demo",
    company_name: "Live AI Chat Support Demo",
    icon: meta,
    iconBg: "#E6DEDD",
    date: "1:00 PM",
    points: [
      "Watch a live demonstration of our AI chat support in action, showing how smart chatbots can answer questions and assist attendees.",
    ],
  },
  {
    title: "Hands-On Tech Workshop",
    company_name: "Hands-On Tech Workshop",
    icon: meta,
    iconBg: "#E6DEDD",
    date: "2:00 PM",
    points: [
      "Participate in a workshop where you can try out futuristic gadgets and learn simple skills to use emerging technologies.",
    ],
  },
  {
    title: "Dynamic Theme Showcase",
    company_name: "Dynamic Theme Showcase",
    icon: meta,
    iconBg: "#E6DEDD",
    date: "3:00 PM",
    points: [
      "Experience how the website adapts its look based on the time of day, offering a fresh, interactive design that enhances your event experience.",
    ],
  },
  {
    title: "Closing Ceremony & Q&A",
    company_name: "Closing Ceremony & Q&A",
    icon: meta,
    iconBg: "#E6DEDD",
    date: "4:00 PM",
    points: [
      "Wrap up the day with a friendly session. Share your thoughts, ask questions, and get a clear summary of the event highlights.",
    ],
  },
];

const testimonials = [
  {
    image: "../src/assets/profile Amol.jpg",
    testimonial:
      "Developer & DSA",
    name: "Amol Gurbhele",
    designation: "STUDENT",
    company: "G.H. Raisoni College",
    
  },
  {
    image: "https://randomuser.me/api/portraits/men/6.jpg",
    testimonial:
      "Cloud Computing",
    name: "Jayant Solao",
    designation: "STUDENT",
    company: "G.H. Raisoni College",
    
  },
  {
    testimonial:
      "Web Dev",
    name: "Himanshu Bidwaik",
    designation: "STUDENT",
    company: "G.H. Raisoni College",
    image: "https://randomuser.me/api/portraits/women/8.jpg",
  },
];

const projects = [
  {
    name: "Car Rent",
    description:
      "Web-based platform that allows users to search, book, and manage car rentals from various providers, providing a convenient and efficient solution for transportation needs.",
    tags: [
      {
        name: "react",
        color: "blue-text-gradient",
      },
      {
        name: "mongodb",
        color: "green-text-gradient",
      },
      {
        name: "tailwind",
        color: "pink-text-gradient",
      },
    ],
    image: carrent,
    source_code_link: "https://github.com/",
  },
  {
    name: "Job IT",
    description:
      "Web application that enables users to search for job openings, view estimated salary ranges for positions, and locate available jobs based on their current location.",
    tags: [
      {
        name: "react",
        color: "blue-text-gradient",
      },
      {
        name: "restapi",
        color: "green-text-gradient",
      },
      {
        name: "scss",
        color: "pink-text-gradient",
      },
    ],
    image: jobit,
    source_code_link: "https://github.com/",
  },
  {
    name: "Trip Guide",
    description:
      "A comprehensive travel booking platform that allows users to book flights, hotels, and rental cars, and offers curated recommendations for popular destinations.",
    tags: [
      {
        name: "nextjs",
        color: "blue-text-gradient",
      },
      {
        name: "supabase",
        color: "green-text-gradient",
      },
      {
        name: "css",
        color: "pink-text-gradient",
      },
    ],
    image: tripguide,
    source_code_link: "https://github.com/",
  },
];

export { services, technologies, experiences, testimonials, projects };
