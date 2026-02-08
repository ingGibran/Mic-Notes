import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { Plus, LogOut } from 'lucide-react';
import { getNotes, createNote, updateNote, deleteNote } from '../api';
import NoteCard from '../components/NoteCard';
import NoteModal from '../components/NoteModal';

const NotesPage = () => {
    const [notes, setNotes] = useState([]);
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [currentNote, setCurrentNote] = useState(null);
    const [isLoading, setIsLoading] = useState(false);
    const navigate = useNavigate();
    const userId = localStorage.getItem('userId');

    useEffect(() => {
        if (!userId) {
            navigate('/');
            return;
        }
        fetchNotes();
    }, [userId, navigate]);

    const fetchNotes = async () => {
        try {
            const data = await getNotes(userId);
            setNotes(data);
        } catch (error) {
            console.error('Error fetching notes:', error);
        }
    };

    const handleCreateOrUpdate = async (noteData) => {
        setIsLoading(true);
        try {
            if (currentNote) {
                await updateNote({ ...noteData, id: currentNote.id });
            } else {
                await createNote({ ...noteData, id_usuario: userId });
            }
            setIsModalOpen(false);
            setCurrentNote(null);
            fetchNotes();
        } catch (error) {
            console.error('Error saving note:', error);
        } finally {
            setIsLoading(false);
        }
    };

    const handleDelete = async (noteId) => {
        if (window.confirm('Are you sure you want to delete this note?')) {
            try {
                await deleteNote(noteId);
                fetchNotes();
            } catch (error) {
                console.error('Error deleting note:', error);
            }
        }
    };

    const openModal = (note = null) => {
        setCurrentNote(note);
        setIsModalOpen(true);
    };

    const handleLogout = () => {
        localStorage.removeItem('userId');
        navigate('/');
    };

    return (
        <div className="min-h-screen bg-gray-50">
            <header className="bg-white shadow-sm sticky top-0 z-10 border-b border-mint-100">
                <div className="max-w-6xl mx-auto px-4 py-4 flex justify-between items-center">
                    <h1 className="text-2xl font-bold text-mint-900 tracking-tight">Mic-Notes</h1>

                    <div className="flex items-center space-x-4">
                        <button
                            onClick={() => openModal()}
                            className="flex items-center space-x-2 bg-mint-500 hover:bg-mint-600 text-white px-4 py-2 rounded-lg font-medium shadow-md hover:shadow-lg transition-all"
                        >
                            <Plus size={20} />
                            <span>New Note</span>
                        </button>
                        <button
                            onClick={handleLogout}
                            className="p-2 text-gray-400 hover:text-gray-600 hover:bg-gray-100 rounded-lg transition-colors"
                            title="Logout"
                        >
                            <LogOut size={20} />
                        </button>
                    </div>
                </div>
            </header>

            <main className="max-w-6xl mx-auto px-4 py-8">
                {notes.length === 0 ? (
                    <div className="text-center py-20">
                        <div className="bg-mint-50 w-24 h-24 rounded-full flex items-center justify-center mx-auto mb-6">
                            <Plus size={40} className="text-mint-300" />
                        </div>
                        <h2 className="text-2xl font-bold text-gray-700 mb-2">No notes yet</h2>
                        <p className="text-gray-500 mb-8">Capture your first idea to get started!</p>
                        <button
                            onClick={() => openModal()}
                            className="text-mint-600 font-semibold hover:underline"
                        >
                            Create your first note
                        </button>
                    </div>
                ) : (
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                        {notes.map((note) => (
                            <NoteCard
                                key={note.id}
                                note={note}
                                onEdit={openModal}
                                onDelete={handleDelete}
                            />
                        ))}
                    </div>
                )}
            </main>

            <NoteModal
                isOpen={isModalOpen}
                onClose={() => setIsModalOpen(false)}
                onSubmit={handleCreateOrUpdate}
                noteToEdit={currentNote}
                isLoading={isLoading}
            />
        </div>
    );
};

export default NotesPage;
