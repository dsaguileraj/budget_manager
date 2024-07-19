interface Props {
  label: string;
  field: Date;
  setField: (value: Date) => void;
  max?: string;
  min?: string;
}

const InputDate: React.FC<Props> = ({ label, field, setField, max, min }) => {
  const id: string = Math.random().toString();
  return (
    <div>
      <label htmlFor={id}>{label}</label>
      <input
        type='date'
        id={id}
        value={field.toISOString().substring(0, 10)}
        onChange={event => setField(new Date(event.target.value))}
        max={max}
        min={min}
        required
      />
    </div>
  );
};

export default InputDate;
