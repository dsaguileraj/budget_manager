interface Option {
  value: string | number;
  label: string;
}

interface Props {
  label: string;
  field: string | number;
  setField: (value: string | number) => void;
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
  return (
    <div>
      <label htmlFor={field.toString()}>{label}</label>
      <select
        id={field.toString()}
        value={field}
        onChange={event => setField(event.target.value)}
        multiple={multiple}
        required={required}
        disabled={disabled}
      >
        {options.map(option => (
          <option
            key={option.value}
            value={option.value}
          >
            {option.label}
          </option>
        ))}
      </select>
    </div>
  );
};

export default InputSelect;
