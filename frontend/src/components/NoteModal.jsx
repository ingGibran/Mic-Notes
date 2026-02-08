import React, { useState, useEffect } from 'react';
import { X } from 'lucide-react';

const NoteModal = ({ isOpen, onClose, onSubmit, noteToEdit, isLoading }) => {
    const [titulo, setTitulo] = useState('');
    const [contenido, setContenido] = useState('');

    useEffect(() => {
        if (noteToEdit) {
            setTitulo(noteToEdit.titulo);
            setContenido(noteToEdit.contenido);
        } else {
            setTitulo('');
            setContenido('');
        }
    }, [noteToEdit, isOpen]);

    if (!isOpen) return null;

    const handleSubmit = (e) => {
        e.preventDefault();
        onSubmit({ titulo, contenido });
    };

    return (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm">
            <div className="bg-white rounded-2xl w-full max-w-lg shadow-2xl transform transition-all scale-100">
                <div className="flex justify-between items-center p-6 border-b border-gray-100">
                    <h2 className="text-xl font-bold text-gray-800">
                        {noteToEdit ? 'Edit Note' : 'New Note'}
                    </h2>
                    <button onClick={onClose} className="text-gray-400 hover:text-gray-600">
                        <X size={24} />
                    </button>
                </div>

                <form onSubmit={handleSubmit} className="p-6 space-y-4">
                    <div>
                        <label className="block text-sm font-semibold text-gray-700 mb-1">Title</label>
                        <input
                            type="text"
                            value={titulo}
                            onChange={(e) => setTitulo(e.target.value)}
                            className="w-full px-4 py-2 rounded-lg border border-gray-200 focus:outline-none focus:ring-2 focus:ring-mint-500 focus:border-transparent transition-all"
                            placeholder="Note title..."
                            required
                        />
                    </div>

                    <div>
                        <label className="block text-sm font-semibold text-gray-700 mb-1">Content</label>
                        <textarea
                            value={contenido}
                            onChange={(e) => setContenido(e.target.value)}
                            className="w-full px-4 py-2 rounded-lg border border-gray-200 focus:outline-none focus:ring-2 focus:ring-mint-500 focus:border-transparent transition-all h-40 resize-none"
                            placeholder="What's on your mind?..."
                            required
                        />
                    </div>

                    <div className="flex justify-end pt-2 space-x-3">
                        <button
                            type="button"
                            onClick={onClose}
                            className="px-5 py-2 text-gray-600 hover:bg-gray-100 rounded-lg font-medium transition-colors"
                        >
                            Cancel
                        </button>
                        <button
                            type="submit"
                            disabled={isLoading}
                            className="px-5 py-2 bg-mint-500 hover:bg-mint-600 text-white rounded-lg font-semibold shadow hover:shadow-lg transition-all"
                        >
                            {isLoading ? 'Saving...' : 'Save Note'}
                        </button>
                    </div>
                </form>
            </div>
        </div>
    );
};

export default NoteModal;
