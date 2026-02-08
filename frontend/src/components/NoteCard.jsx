import React from 'react';
import { Pencil, Trash2 } from 'lucide-react';

const NoteCard = ({ note, onEdit, onDelete }) => {
    return (
        <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-100 hover:shadow-md transition-shadow group relative overflow-hidden">
            <div className="absolute top-0 left-0 w-1 h-full bg-mint-400 opacity-0 group-hover:opacity-100 transition-opacity"></div>

            <div className="flex justify-between items-start mb-4">
                <h3 className="text-lg font-bold text-gray-800 line-clamp-1">{note.titulo}</h3>
                <div className="flex space-x-2 opacity-0 group-hover:opacity-100 transition-opacity">
                    <button
                        onClick={() => onEdit(note)}
                        className="p-1.5 text-gray-400 hover:text-mint-600 hover:bg-mint-50 rounded-full transition-colors"
                    >
                        <Pencil size={16} />
                    </button>
                    <button
                        onClick={() => onDelete(note.id)}
                        className="p-1.5 text-gray-400 hover:text-red-500 hover:bg-red-50 rounded-full transition-colors"
                    >
                        <Trash2 size={16} />
                    </button>
                </div>
            </div>

            <p className="text-gray-600 text-sm line-clamp-4 leading-relaxed whitespace-pre-wrap">
                {note.contenido}
            </p>
        </div>
    );
};

export default NoteCard;
