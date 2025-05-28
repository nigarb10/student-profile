{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c49d68f1-926a-406f-bdb7-049f6cc57ad1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Profile created successfully\n"
     ]
    }
   ],
   "source": [
    "def create_profile(name, student_id, bio):\n",
    "    with open('student_profile.txt', 'w') as f:\n",
    "        f.write(f\"Name: {name}\\n\")\n",
    "        f.write(f\"Student ID: {student_id}\\n\")\n",
    "        f.write(f\"Bio: {bio}\\n\")\n",
    "    print(\"Profile created successfully\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    create_profile(\"Nigar Bizanjo\", \"123456\", \"I am a student learning software construction.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4f8991d0-cbf4-48aa-92bc-3581b6fdebd5",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
