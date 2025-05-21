export default function EntityForm({ onSubmit, fields, initialData = {} }) {
  const handleSubmit = (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const data = {};
    fields.forEach(field => {
      data[field.name] = formData.get(field.name) || initialData[field.name];
    });
    onSubmit(data);
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      {fields.map(field => (
        <div key={field.name}>
          <label className="block">{field.label}</label>
          <input
            type={field.type || 'text'}
            name={field.name}
            defaultValue={initialData[field.name] || ''}
            className="border p-2 w-full"
            required={field.required}
          />
        </div>
      ))}
      <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded">
        Submit
      </button>
    </form>
  );
}