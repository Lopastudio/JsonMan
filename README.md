# JsonMan

JsonMan is a simple Python script for managing a key-value data store with JSON file persistence. Written by [Patrik Nagy](https://www.lopastudio.sk) on 2.11.2023.

## Features

- **Add**: Add key-value pairs to the data store.
- **Remove**: Remove either a key or a value associated with a key from the data store.
- **View**: View the value associated with a specific key.
- **Edit**: Edit the value associated with a specific key.
- **Save**: Save the current state of the data store to a JSON file.
- **Load**: Load data from a JSON file into the data store.

## Usage

### Add Data

```python
add(key, value)
```

Adds a key-value pair to the data store.

### Remove Data

```python
remove(key, value)
```

Removes either a key or the value associated with a key from the data store. The user is prompted to confirm the removal.

### View Data

```python
view(key)
```

Displays the value associated with a specific key in the data store.

### Edit Data

```python
edit(key, new_value)
```

Edits the value associated with a specific key in the data store.

### Save Data

```python
save(filename)
```

Saves the current state of the data store to a JSON file.

### Load Data

```python
load(filename)
```

Loads data from a JSON file into the data store.

## Example

```python
# Adding data
add("name", "John Doe")

# Viewing data
view("name")

# Editing data
edit("name", "Jane Doe")

# Saving data to a file
save("data.json")

# Loading data from a file
load("data.json")
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
