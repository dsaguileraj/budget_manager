import { BrowserRouter, Route, Routes } from 'react-router-dom';
// import { Navigation } from './components/Navigation.jsx';
import ProcedurePOST from './pages/create/ProcedurePOST';

function App() {
  return (
    <BrowserRouter>
      {/* <Navigation /> */}
      <Routes>
        <Route path='/procedure/create' element={<ProcedurePOST />} />
      </Routes>
    </BrowserRouter>
  );
}
export default App;