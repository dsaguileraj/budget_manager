import { useParams } from "react-router-dom";

const Procedure: React.FC = () => {
  const params = useParams();
  return <h1>Procedure: {params.id}</h1>;
};

export default Procedure;
