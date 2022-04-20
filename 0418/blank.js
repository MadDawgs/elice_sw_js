// 내비게이션 바 레이아웃을 설계하세요.
const Nav = () => {
    return 
        <nav>
            <a class="logo" href="#"><img src ="logo.png"></a>
            <input type="text" class="search" placeholder="Search"></input>
            <span class="nav-links">
                <a href="#"><img src="home.png"></a>
                <a href="#"><img src="message.png"></a>
                <a href="#"><img src="compass.png"></a>
                <a href="#"><img src="heart.png"></a>
            </span>
        </nav>
    
}  

export default Nav