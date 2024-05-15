import { Route, BrowserRouter as Router, Routes } from 'react-router-dom';

import Home from './Home';

function App() {
	return (
		<Router>
			<Routes>
				<Route path='/' element={<Home></Home>}></Route>
			</Routes>
		</Router>
	);
}

export default App;
