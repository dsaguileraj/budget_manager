interface Props {
  label: string;
  field: boolean;
  setField: (value: boolean) => void;
  required?: boolean;
  disabled?: boolean;
}

const InputCheck: React.FC<Props> = ({
  label,
  field,
  setField,
  required = true,
  disabled = false,
}) => {
  return (
    <div>
      <label htmlFor={field.toString()}>{label}</label>
      <input
        type='number'
        id={field.toString()}
        value={field.toString()}
        onChange={event => setField(event.target.checked)}
        required={required}
        disabled={disabled}
      />
    </div>
  );
};

export default InputCheck;
