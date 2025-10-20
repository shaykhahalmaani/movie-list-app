import { render, screen } from '@testing-library/react';
import MovieList from '../MovieList';

test('renders movie list', () => {
  const mockOnMovieClick = jest.fn();
  render(<MovieList onMovieClick={mockOnMovieClick} />);
  // Add more specific tests here
});
