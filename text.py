{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a41fdd35",
   "metadata": {},
   "outputs": [],
   "source": [
    "def my_func(x1,x2,x3):\n",
    "    \n",
    "    if  isinstance(x1,float)== False or isinstance(x2,float)== False or isinstance(x3,float)== False:\n",
    "        return (\"Error: parameters should be float\")\n",
    "    elif x1+ x2 + x3 == 0 :\n",
    "        return (\"Not a number – denominator equals zero\")\n",
    "    else :\n",
    "        ans = ((x1+x2+x3)*(x2+x3)*x3)/(x1+x2+x3)\n",
    "        return ans\n",
    "    \n",
    "    \n",
    "def convert(hours, minutes):\n",
    "    if hours<0 or minutes<0:\n",
    "        return \"Input error!\"\n",
    "    else:\n",
    "        return hours*3600 + minutes*60"
   ]
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
