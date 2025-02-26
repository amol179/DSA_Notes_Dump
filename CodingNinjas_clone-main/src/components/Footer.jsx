// import React from 'react'

const Footer = () => {
  return (
    <div className='bg-[#27211e] h-[840px] w-screen flex flex-col gap-6 '>
      <span className="ml-[270px] mt-28 text-white text-2xl">Important Links</span>
      
      <div className="ml-[270px] flex items-center gap-20">
        <span className="text-white text-sm">Job Bootcamp for<br/>  professionals</span>
        <a href="#" className=" text-gray-500 underline text-sm font-bold mt-[-23px]">Web Development Bootcamp (MERN & Springboot) |  Data Analytics Job Bootcamp</a>
      </div>
      
      <div className="ml-[270px] flex items-center gap-20">
        <span className="text-white text-sm">IIT Certifications for<br/>  professionals</span>
        <a href="#" className=" text-gray-500 underline text-sm font-bold mt-[-23px]">PG Certification in Data Analytics by E&ICT Academy, IIT Guwahati</a>
      </div>
      
      <div className="ml-[270px] flex items-center gap-20">
        <span className="text-white text-sm">IIT Certifications for<br/>  Students</span>
        <div className="flex flex-col gap-9 mt-9" >
        <a href="#" className=" text-gray-500 underline text-sm font-bold mt-[-23px]">Training and Internship Certification in Data Analytics by E&ICT Academy, IIT Guwahati
        |</a>
        <a href="#" className=" text-gray-500 underline text-sm font-bold mt-[-23px]">Training and Internship Certification in Advanced DSA by E&ICT Academy, IIT Guwahati</a>
        </div>
      </div>
      
      <div className="ml-[270px] flex flex-row items-center gap-20">
        <span className="text-white text-sm">We accept payments using:</span>
        <div className="flex flex-row items-center justify-between gap-36">
          <div className="flex flex-row gap-3 h-4">
            <div className="h-6 w-14 rounded-md bg-white flex items-center justify-center">
            <img src="/public/icons/visa.png" className="h-3 " alt="" />
            </div>
            <div className="h-6 w-14 rounded-md bg-white flex items-center justify-center">
            <img src="/public/icons/paypal.png" className="h-3 " alt="" />
            </div>
            <div className="h-6 w-14 rounded-md bg-white flex items-center justify-center">
            <img src="/public/icons/upi.png" className="h-3 " alt="" />
            </div>
            <div className="h-6 w-14 rounded-md bg-white flex items-center justify-center">
            <img src="/public/icons/no-cost-emi.png" className="h-3 " alt="" />
            </div>
            
            
            
          </div>
          <div className="flex flex-row gap-3">
            <img src="/public/icons/secure.png" alt="" />
            <div className="h-6 w-16 rounded-md bg-white flex items-center justify-center">
            <img src="/public/icons/razorpay.png" className="p-2" alt="" />
            </div>
            
          </div>
        </div>
      </div>
      <h1 className="flex items-center justify-center text-9xl font-bold mt-36 text-neutral-400 opacity-5">Coding Ninjas</h1>
    </div>
  )
}

export default Footer
