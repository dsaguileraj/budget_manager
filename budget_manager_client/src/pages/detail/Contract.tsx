import { useParams } from "react-router-dom";

const Contract: React.FC = () => {
  const params = useParams();
  return <h1>Contract: {params.id}</h1>;
};

export default Contract;
