// import React from 'react'


const Manager = () => {

    return (
        <>
            <div className='  bg-[#252525] bg-[radial-gradient(#ffffff33_1px,#00091d_1px)] bg-[size:20px_20px]'>

                <div className="flex flex-col items-center  p-2 md:p-0 h-screen  relative bg">
                    {/* <div className="absolute top-0 z-[-2] h-[1250px] w-screen bg-[#000000] bg-[radial-gradient(#ffffff33_1px,#00091d_1px)] bg-[size:20px_20px]"></div> */}

                    <h1 className="text-3xl mt-28 py-4 text-white text-center animate-colorChange">
                        Restricted by opportunities?
                    </h1>

                    <p className="text-white py-4 font-bold text-7xl text-center">
                        Get the tech career <br /> you deserve. Faster.
                    </p>

                    <p className="text-gray-500 py-4 mb-9 text-lg text-center">
                        Structured coding courses that get you there faster with confidence.
                    </p>

                    <button className="px-6 py-3 flex items-center justify-center bg-orange-500 text-white font-bold text-xl rounded-lg hover:bg-orange-400">
                        Explore offerings
                        <span className="ml-2"><img className='h-5 text-gray-300' src="/icons/arrow.png" alt="" /></span>
                    </button>

                    <video className="w-full max-w-[995px] rounded-lg mt-32" autoPlay muted loop>
                        <source src="/icons/video.mp4" type="video/mp4" />
                        Your browser does not support the video tag.
                    </video>
                </div>

                <div className="flex px-64 mt-[509px] h-[600px] mb-[-326px]  w-screen bg-slate-50 ">
                    <h2 className="mt-[60px] text-[112px] font-bold text-black opacity-15  text-start flex gap-16">
                        <div className="border-l-2 border-dotted border-black h-72 mt-[-50px]"></div>
                        OUR OFFERINGS
                    </h2>
                </div>

                <div className="bg-slate-50">
                    <div className="mt-6 max-w-3xl w-full flex items-start bg-slate-50">
                        <img src="/public/icons/bootcampicon.svg" className='px-[204px] mt-[-45px]' alt="" />

                        <p className="text-xl flex items-center justify-center ml-[-226px] mt-[-18px] gap-3 text-black font-bold bg-slate-50">
                            Job Bootcamp <br />
                            <span className="text-sm text-black rounded-e-full h-7 w-32 text-center flex items-center justify-center bg-blue-200">For graduates</span>
                        </p>

                    </div>

                    <div className="flex px-64">
                        <div className="border-l-2 border-dotted border-black h-72  mt-[-50px]"></div>

                        <div className="px-9 flex flex-col md:flex-row justify-center gap-8">
                            {/* card 1 */}
                            <button className="w-[434px] h-44 rounded-lg cursor-pointer">

                                <div className="bg-blue-50 flex flex-row items-center justify-center h-32 gap-2 ">
                                    <div className="bg-white h-20 w-20 rounded-full p-2 ">
                                        <img
                                            src="/public/icons/fullstack.svg"
                                            alt="Full Stack Web Development"
                                            className=" h-12 w-12 items-center justify-center mt-2 ml-2"
                                        />
                                    </div>
                                    <h3 className="text-lg font-bold mt-4 ">Full Stack Web Development with <br /> GenAI</h3>
                                </div>
                               
                                <div className="bg-white p-2 flex flex-row gap-6">
                                    <p className="text-gray-700">140+ Hrs of content</p>
                                    <p className="text-gray-700">600+ Problems</p>
                                    <p className="text-gray-700">10k+ Learners</p>
                                </div>
                            </button> 
                           
                            {/* card 2 */}
                            <div className="w-[434px] h-44 rounded-lg overflow-hidden shadow-lg">

                                <div className="bg-blue-50 flex flex-row items-center justify-center h-32 gap-2 ">
                                    <div className="bg-white h-20 w-20 rounded-full p-2 ">
                                        <img
                                            src="/public/icons/fullstack.svg"
                                            alt="Full Stack Web Development"
                                            className=" h-12 w-12 items-center justify-center mt-2 ml-2"
                                        />
                                    </div>
                                    <h3 className="text-lg font-bold mt-4 ">Full Stack Web Development with <br /> GenAI</h3>
                                </div>
                                {/* Lower Section */}
                                <div className="bg-white p-2 flex flex-row gap-6">
                                    <p className="text-gray-700">140+ Hrs of content</p>
                                    <p className="text-gray-700">600+ Problems</p>
                                    <p className="text-gray-700">10k+ Learners</p>
                                </div>
                            </div>

                        </div>


                    </div>
                </div>

                <div className='bg-[#f8f8ef] h-[1231px]'>
                    <div className="border-l-2 border-dotted border-black h-16 ml-64  "></div>
                    <div className="mt-6 max-w-3xl w-full flex items-start">
                        <img src="/public/icons/scroll.svg" className='px-[236px] mt-[-24px]' alt="" />

                        <p className="text-xl flex flex-col items-start  ml-[-226px] mt-[-18px] gap-9 text-black font-bold">
                            IIT Certifications <br />
                            <span className="text-sm text-[#f8916c] rounded-full h-8 w-32 flex items-center justify-center bg-[#745e39]">For graduates</span>
                        </p>
                    </div>

                    <div className="flex">
                        <button className="w-72 h-[380px] rounded-lg overflow-hidden shadow-lg border border-[#e0c7bc] ml-72 mt-5">

                            <div className="bg-slate-100 flex flex-col items-center h-80 gap-2  ">
                                <div className="bg-slate-100">
                                    <img
                                        src="/public/icons/iitimage.png"
                                        alt=""
                                        className="mt-2 p-3"
                                    />
                                </div>

                                <div className="bg-white ml-[-199px] mt-[-41px] h-9 w-9 rounded-md ">
                                    <img src="/public/icons/frame.svg" className=' mt-1 ml-1' alt="" />
                                </div>

                                <h3 className="text-lg font-bold text-start ml-4  p-2">PG Certification in Data Analytics with GenAI</h3>
                                <span className="text-sm text-[#4f4642] rounded-e-full h-8 w-52 ml-[-29px] flex items-center justify-center bg-[#f8f7f5]">E&ICT Academy, IIT Guwahati</span>
                            </div>

                            <hr className="border-gray-300 mx-4 bg-slate-100" />

                            <div className="bg-slate-100 p-5 flex  flex-row gap-6">
                                <div className="flex  justify-between">
                                    <div className="flex gap-2">
                                        <img src="/public/icons/chatgpt.png" alt="" />
                                        <img src="/public/icons/meta.svg" alt="" />
                                        <img src="/public/icons/meta1.svg" alt="" />
                                    </div>
                                    <div className="ml-14">
                                        <p className="text-gray-700 text-sm">6 months</p>
                                    </div>
                                </div>
                            </div>
                        </button>


                        <button className="w-72 h-[380px] rounded-lg overflow-hidden shadow-lg border border-[#e0c7bc] ml-8 mt-5">

                            <div className="bg-slate-100 flex flex-col items-center h-80 gap-2  ">
                                <div className="bg-slate-100">
                                    <img
                                        src="/public/icons/iitimage.png"
                                        alt=""
                                        className="mt-2 p-3"
                                    />
                                </div>

                                <div className="bg-white ml-[-199px] mt-[-41px] h-9 w-9 rounded-md ">
                                    <img src="/public/icons/frame1.webp" className=' rounded-md' alt="" />
                                </div>

                                <h3 className="text-lg text-start ml-3 font-bold  p-3">PG Certification in Full Stack Web Development with Generative AI</h3>
                                <span className="text-sm text-[#4f4642] rounded-e-full h-8 w-32 ml-[-122px] flex items-center justify-center bg-[#f8f7f5]">IITM Pravartak</span>
                            </div>

                            <hr className="border-gray-300 mx-4 bg-slate-100" />

                            <div className="bg-slate-100 p-5 flex  flex-row gap-6">
                                <div className="flex  justify-between">
                                    <div className="flex gap-2">
                                        <img src="/public/icons/meta3.png" className='h-6 w-6' alt="" />
                                        <img src="/public/icons/meta4.png" className='h-6 w-6' alt="" />
                                        <img src="/public/icons/meta5.png" className='h-6 w-6' alt="" />
                                        <img src="/public/icons/meta6.png" className='h-6 w-6' alt="" />
                                    </div>
                                    <div className="ml-14">
                                        <p className="text-gray-700 text-sm">9 months</p>
                                    </div>
                                </div>
                            </div>
                        </button>

                    </div>
                    <span className="text-sm font-bold text-[#f8916c] rounded-full h-6 w-40 flex items-center justify-center bg-[#745e39] ml-72 mt-9">For college students
                    </span>

                    <div className="flex">
                        <button className="w-72 h-[380px] rounded-lg overflow-hidden shadow-lg border border-[#e0c7bc] ml-72 mt-5">

                            <div className="bg-slate-100 flex flex-col items-center h-80 gap-2  ">
                                <div className="bg-slate-100">
                                    <img
                                        src="/public/icons/iitimage.png"
                                        alt=""
                                        className="mt-2 p-3"
                                    />
                                </div>

                                <div className="bg-white ml-[-199px] mt-[-41px] h-9 w-9 rounded-md ">
                                    <img src="/public/icons/frame.svg" className=' mt-1 ml-1' alt="" />
                                </div>

                                <h3 className="text-lg font-bold text-start ml-2  p-3">Training and Internship Certification in Advanced DSA
                                </h3>
                                <span className="text-sm text-[#4f4642] rounded-e-full h-8 w-32 ml-[-122px] flex items-center justify-center bg-[#f8f7f5]">IITM Pravartak</span>
                            </div>

                            <hr className="border-gray-300 mx-4 bg-slate-100" />

                            <div className="bg-slate-100 p-5 flex  flex-row gap-6">
                                <div className="flex  justify-between">
                                    <div className="flex gap-2">
                                        <img src="/public/icons/meta3.png" className='h-6 w-6' alt="" />
                                        <img src="/public/icons/meta4.png" className='h-6 w-6' alt="" />
                                        <img src="/public/icons/meta5.png" className='h-6 w-6' alt="" />
                                        <img src="/public/icons/meta6.png" className='h-6 w-6' alt="" />
                                    </div>
                                    <div className="ml-14">
                                        <p className="text-gray-700 text-sm">4 months</p>
                                    </div>
                                </div>
                            </div>
                        </button>


                        <button className="w-72 h-[380px] rounded-lg overflow-hidden shadow-lg border border-[#e0c7bc] ml-8 mt-5">

                            <div className="bg-slate-100 flex flex-col items-center h-80 gap-2  ">
                                <div className="bg-slate-100">
                                    <img
                                        src="/public/icons/iitimage.png"
                                        alt=""
                                        className="mt-2 p-3"
                                    />
                                </div>

                                <div className="bg-white ml-[-199px] mt-[-41px] h-9 w-9 rounded-md ">
                                    <img src="/public/icons/frame1.webp" className=' rounded-md' alt="" />
                                </div>

                                <h3 className="text-lg font-bold text-start ml-2  p-3">Training and Internship Certification in Data Analytics
                                </h3>
                                <span className="text-sm text-[#4f4642] rounded-e-full h-8 w-52 ml-[-22px] flex items-center justify-center bg-[#f8f7f5]">E&ICT Academy, IIT Guwahati</span>
                            </div>

                            <hr className="border-gray-300 mx-4 bg-slate-100" />

                            <div className="bg-slate-100 p-5 flex  flex-row gap-6">
                                <div className="flex  justify-between">
                                    <div className="flex gap-2">
                                        <img src="/public/icons/meta2.png" className='h-6 w-6' alt="" />
                                        <img src="/public/icons/meta7.png" className='h-6 w-6' alt="" />
                                        <img src="/public/icons/meta8.png" className='h-6 w-6' alt="" />
                                        <img src="/public/icons/meta1.svg" className='h-6 w-6' alt="" />
                                    </div>
                                    <div className="ml-14">
                                        <p className="text-gray-700 text-sm">6 months</p>
                                    </div>
                                </div>
                            </div>
                        </button>


                        <button className="w-72 h-[380px] rounded-lg overflow-hidden shadow-lg border border-[#e0c7bc] ml-8 mt-5">

                            <div className="bg-slate-100 flex flex-col items-center h-80 gap-2  ">
                                <div className="bg-slate-100">
                                    <img
                                        src="/public/icons/iitimage.png"
                                        alt=""
                                        className="mt-2 p-3"
                                    />
                                </div>

                                <div className="bg-white ml-[-199px] mt-[-41px] h-9 w-9 rounded-md ">
                                    <img src="/public/icons/frame1.webp" className=' rounded-md' alt="" />
                                </div>

                                <h3 className="text-lg font-bold text-start ml-2  p-3">Training and Internship Certification in Full Stack Web Development

                                </h3>
                                <span className="text-sm text-[#4f4642] rounded-e-full h-8 w-32 ml-[-122px] flex items-center justify-center bg-[#f8f7f5]">IITM Pravartak</span>
                            </div>

                            <hr className="border-gray-300 mx-4 bg-slate-100" />

                            <div className="bg-slate-100 p-5 flex  flex-row gap-6">
                                <div className="flex  justify-between">
                                    <div className="flex gap-2">
                                        <img src="/public/icons/meta3.png" className='h-6 w-6' alt="" />
                                        <img src="/public/icons/meta4.png" className='h-6 w-6' alt="" />
                                        <img src="/public/icons/meta5.png" className='h-6 w-6' alt="" />
                                        <img src="/public/icons/meta6.png" className='h-6 w-6' alt="" />
                                    </div>
                                    <div className="ml-14">
                                        <p className="text-gray-700 text-sm">6 months</p>
                                    </div>
                                </div>
                            </div>
                        </button>

                    </div>
                    <img src="/public/icons/mask-group.png" alt="" />


                </div>







            </div>


        </>
    )
}

export default Manager
