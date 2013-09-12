"""autogenerated by genpy from graspit_msgs/GraspStatus.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class GraspStatus(genpy.Message):
  _md5sum = "88d06ce7ea2a1be53f7072dbaa262a0b"
  _type = "graspit_msgs/GraspStatus"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """uint8 grasp_status
string status_msg
float64 grasp_identifier
uint8 FAILED = 0
uint8 SUCCESS = 1
uint8 UNREACHABLE = 2
uint8 OBJECTERROR = 4
uint8 ROBOTERROR = 8
uint8 ENDEFFECTORERROR = 16
uint8 GRASPERROR = 32
uint8 PREGRASPERROR = 64

"""
  # Pseudo-constants
  FAILED = 0
  SUCCESS = 1
  UNREACHABLE = 2
  OBJECTERROR = 4
  ROBOTERROR = 8
  ENDEFFECTORERROR = 16
  GRASPERROR = 32
  PREGRASPERROR = 64

  __slots__ = ['grasp_status','status_msg','grasp_identifier']
  _slot_types = ['uint8','string','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       grasp_status,status_msg,grasp_identifier

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GraspStatus, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.grasp_status is None:
        self.grasp_status = 0
      if self.status_msg is None:
        self.status_msg = ''
      if self.grasp_identifier is None:
        self.grasp_identifier = 0.
    else:
      self.grasp_status = 0
      self.status_msg = ''
      self.grasp_identifier = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      buff.write(_struct_B.pack(self.grasp_status))
      _x = self.status_msg
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_d.pack(self.grasp_identifier))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      start = end
      end += 1
      (self.grasp_status,) = _struct_B.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.status_msg = str[start:end].decode('utf-8')
      else:
        self.status_msg = str[start:end]
      start = end
      end += 8
      (self.grasp_identifier,) = _struct_d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      buff.write(_struct_B.pack(self.grasp_status))
      _x = self.status_msg
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_d.pack(self.grasp_identifier))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      start = end
      end += 1
      (self.grasp_status,) = _struct_B.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.status_msg = str[start:end].decode('utf-8')
      else:
        self.status_msg = str[start:end]
      start = end
      end += 8
      (self.grasp_identifier,) = _struct_d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_B = struct.Struct("<B")
_struct_d = struct.Struct("<d")