import React from 'react';

const Header = () => {
   const margem = {margin:'20px'}
     return(
        <div style={{ display:"flex", margin:'20px'}}>
        <h1 style={margem}>Logo GSW</h1>
        <input style={margem}></input>
            <div style={margem}>
               Link 1
           </div>
           <div style={margem}>Redes Sociais</div>
        </div>
     )

};

export default Header;

