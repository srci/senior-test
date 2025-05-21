
  // components/EntityTable.js
  import React from 'react';

  export default function EntityTable({ entities, fields, onDelete }) {
    const dataToRender = Array.isArray(entities) ? entities : [];
  
    return (
      <table className="w-full border-collapse border">
        <thead>
          <tr>
            {fields.map(field => (
              <th key={field.key} className="border p-2 text-left">{field.label}</th>
            ))}
            <th className="border p-2 text-center">Actions</th>
          </tr>
        </thead>
        <tbody>
          {dataToRender.length === 0 ? (
            <tr>
              <td colSpan={fields.length + 1} className="border p-4 text-center text-gray-500">
                No entities to show.
              </td>
            </tr>
          ) : (
            dataToRender.map(entity => (
              <tr key={entity.id}>
                {/* MODIFICACIÓN: Usamos entity[field.key] */}
                {fields.map(field => (
                  <td key={field.key} className="border p-2">{entity[field.key]}</td>
                ))}
                <td className="border p-2 text-center">
                  <button
                    onClick={() => onDelete(entity.id)}
                    className="bg-red-500 hover:bg-red-700 text-white font-bold py-1 px-3 rounded text-sm"
                  >
                    Delete
                  </button>
                </td>
              </tr>
            ))
          )}
        </tbody>
      </table>
    );
  }