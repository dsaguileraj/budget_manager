interface Props {
  label: string;
  field: number | string | undefined;
  setField: (value: number) => void;
  max?: number;
  min?: number;
  required?: boolean;
  disabled?: boolean;
}

const InputNumber: React.FC<Props> = ({
  label,
  field,
  setField,
  max,
  min,
  required = true,
  disabled = false,
}) => {
  const id: string = Math.random().toString();
  return (
    <div>
      <label htmlFor={id}>{label}</label>
      <input
        type='number'
        id={id}
        value={field}
        onChange={event => setField(Number(event.target.value))}
        max={max}
        min={min}
        required={required}
        disabled={disabled}
      />
    </div>
  );
};

export default InputNumber;
