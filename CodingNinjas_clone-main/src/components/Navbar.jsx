// import React from 'react'

const Navbar = () => {
  return (
    <nav className="fixed top-0 left-0 w-full bg-white text-white shadow-lg z-50">
    <div className="container  mx-auto flex justify-between items-center h-16 px-36 ">
    
      <div className=" flex items-center space-x-8">
       
        <div className="flex items-center">
          <img
            src="/public/icons/logo.svg"
            alt="Logo"
            className=""
          />
          
        </div>

        
        <div className="flex space-x-4 items-center">
          
          <button className="flex items-center bg-white hover:bg-gray-200 text-gray-800 py-2 px-4 rounded-xl text-lg">
            Job Bootcamp
            <span className="ml-2"><img className='h-5 text-black' src="/public/icons/down-arrow.png" alt="" /></span> 
          </button>

          
          <button className="flex items-center bg-white hover:bg-gray-200 text-gray-800 py-2 px-4 rounded-xl text-lg">
            IIT Certification
            <span className="ml-2"><img className='h-5 text-gray-300' src="/public/icons/down-arrow.png" alt="" /></span>
          </button>
        </div>
      </div>

      {/* Right Section: Login Button */}
      <button className="bg-orange-500 hover:bg-orange-400 text-white py-2 px-4 rounded-xl text-lg">
        Login
      </button>
    </div>
  </nav>
  )
}

export default Navbar
