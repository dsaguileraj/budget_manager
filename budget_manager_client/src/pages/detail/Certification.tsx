import { useParams } from "react-router-dom";

const Certification: React.FC = () => {
  const params = useParams();
  return <h1>Certification: {params.id}</h1>;
};

export default Certification;
