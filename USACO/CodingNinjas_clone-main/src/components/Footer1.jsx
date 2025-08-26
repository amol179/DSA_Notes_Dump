// import React from 'react'

const Footer1 = () => {
    return (
        <div className="h-[700px] w-screen bg-[#2d231e] ">
            <div className="flex flex-col items-center">
                <div className="flex flex-row items-start justify-between gap-14  px-80">
                    <div className="flex flex-col mt-28">
                        <img src="/public/icons/logo2.svg" className="h-7 ml-[-60px]" alt="" />
                        <span className="text-sm font-bold text-white mt-10">Contact us</span>
                        <div className="flex flex-row gap-4 mt-5">
                            <img src="/public/icons/phone.svg" alt="" />
                            <h1 className="text-xl text-gray-500 hover:text-gray-700 cursor-pointer">1800-123-3598</h1>
                        </div>
                        <div className="flex flex-row gap-4 mt-2">
                            <img src="/public/icons/email.svg" alt="" />
                            <h1 className="text-xl text-gray-500 hover:text-gray-700 cursor-pointer">contact@codingninjas.com</h1>
                        </div>

                        <span className="text-sm font-bold text-white mt-10">Our offerings</span>

                        <div className="flex flex-row gap-4 mt-5">
                            <img src="/public/icons/logo3.svg" className="h-9" alt="" />

                        </div>

                        <div className="flex flex-row gap-4 mt-6">
                            <img src="/public/icons/logo4.webp" className="h-7" alt="" />

                        </div>
                    </div>
                    <div className="flex flex-col mt-28 gap-4">
                        <h1 className="text-sm text-white font-bold">Coding Ninjas</h1>
                        <a href="#" className="text-sm text-gray-500 hover:text-gray-700  cursor-pointer">Careers</a>
                        <a href="#" className="text-sm text-gray-500 hover:text-gray-700  cursor-pointer">Privacy policy</a>
                        <a href="#" className="text-sm text-gray-500 hover:text-gray-700  cursor-pointer">Terms & conditions</a>
                        <a href="#" className="text-sm text-gray-500 hover:text-gray-700  cursor-pointer">Pricing & refund policy</a>
                        <a href="#" className="text-sm text-gray-500 hover:text-gray-700  cursor-pointer">Bug bounty</a>
                        <a href="#" className="text-sm text-gray-500 hover:text-gray-700  cursor-pointer">Review</a>
                        <a href="#" className="text-sm text-gray-500 hover:text-gray-700  cursor-pointer">Press release</a>


                    </div>

                    <div className="flex flex-col mt-28 gap-4">
                        <h1 className="text-sm text-white font-bold">Products</h1>
                        <a href="#" className="text-sm text-gray-500 hover:text-gray-700  cursor-pointer">Job Bootcamp</a>
                        <a href="#" className="text-sm text-gray-500 hover:text-gray-700  cursor-pointer">Code 360</a>
                        <a href="#" className="text-sm text-gray-500 hover:text-gray-700  cursor-pointer">Professional Certifications</a>
                        <a href="#" className="text-sm text-gray-500 hover:text-gray-700  cursor-pointer">Student Certifications</a>



                    </div>

                    <div className="flex flex-col mt-28 gap-4">
                        <h1 className="text-sm text-white font-bold">Community</h1>
                        <a href="#" className="text-sm text-gray-500 hover:text-gray-700  cursor-pointer">10X Club</a>
                        <a href="#" className="text-sm text-gray-500 hover:text-gray-700  cursor-pointer">Student Chapters</a>
                        <a href="#" className="text-sm text-gray-500 hover:text-gray-700  cursor-pointer">Hire from us</a>

                    </div>
                </div>
                <hr className="border-sm w-[853px] border-white opacity-25  mt-12" />
               
            </div>
            <div className="flex items-center justify-between px-[335px] mt-8">
                    <span className="text-gray-500" >Copyright © Sunrise Mentors Pvt. Ltd.</span>
                    <div className="flex gap-4">
                        <img src="/public/icons/insta.svg" alt="" />
                        <img src="/public/icons/facb.svg" alt="" />
                        <img src="/public/icons/linkd.svg" alt="" />
                        <img src="/public/icons/twit.svg" alt="" />
                        <img src="/public/icons/ytub.svg" alt="" />
                    </div>
                    
                </div>

        </div>
    )
}

export default Footer1
