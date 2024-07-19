import { Option } from "../../../../utils/interfaces";

interface Props {
  label: string;
  field: string | number | undefined;
  setField: (value: string | number | undefined) => void;
  options: Option[];
  multiple?: boolean;
  required?: boolean;
  disabled?: boolean;
}

const InputSelect: React.FC<Props> = ({
  label,
  field,
  setField,
  options,
  multiple = false,
  required = true,
  disabled = false,
}) => {
  const id: string = Math.random().toString();
  return (
    <div>
      <label htmlFor={id}>{label}</label>
      <select
        id={id}
        value={field}
        onChange={event => setField(event.target.value)}
        multiple={multiple}
        required={required}
        disabled={disabled}
      >
        {options.map((option, index) => (
          <option
            key={index}
            value={option.value}
            disabled={option.disabled}
          >
            {option.label}
          </option>
        ))}
      </select>
    </div>
  );
};

export default InputSelect;
