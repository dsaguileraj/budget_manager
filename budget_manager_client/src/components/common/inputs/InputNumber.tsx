interface Props {
  label: string;
  field: number;
  setField: (value: number) => void;
  max?: number | undefined;
  min?: number | undefined;
  required?: boolean;
  disabled?: boolean;
}

const InputNumber: React.FC<Props> = ({
  label,
  field,
  setField,
  max = undefined,
  min = undefined,
  required = true,
  disabled = false,
}) => {
  return (
    <div>
      <label htmlFor={field.toString()}>{label}</label>
      <input
        type='number'
        id={field.toString()}
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
