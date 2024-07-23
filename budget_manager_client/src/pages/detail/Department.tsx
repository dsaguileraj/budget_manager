import { useParams } from "react-router-dom";

const Department: React.FC = () => {
  const params = useParams();
  return <h1>Department: {params.id}</h1>;
};

export default Department;
