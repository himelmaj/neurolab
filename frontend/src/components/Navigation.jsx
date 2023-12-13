import React from "react";
import { Link } from "react-router-dom";
import { FaHouseUser } from "react-icons/fa";
import { FaUser } from "react-icons/fa";
import { BiSolidUserBadge } from "react-icons/bi";
import { IoIosHelpCircle } from "react-icons/io";


export function Navigation() {
  return (
    <nav>
      <Link to="/"><FaHouseUser style={{fontSize:'50px' }} /></Link>
      <Link to="/contacto"><BiSolidUserBadge style={{fontSize:'50px' }}/></Link>
      <Link to="/ayuda"><IoIosHelpCircle style={{fontSize:'50px' }}/></Link>
      <Link to="/login"><FaUser style={{fontSize:'50px' }}/></Link>
    </nav>
  );
}
