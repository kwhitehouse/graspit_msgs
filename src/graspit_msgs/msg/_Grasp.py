"""autogenerated by genpy from graspit_msgs/Grasp.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg

class Grasp(genpy.Message):
  _md5sum = "5cc193efa0164eb4eda97d55f28827a0"
  _type = "graspit_msgs/Grasp"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """float64 epsilon_quality
float64 volume_quality
float64[] secondary_qualities
int32 grasp_source
int32 grasp_group
int32 grasp_type
geometry_msgs/Pose pre_grasp_pose
geometry_msgs/Pose final_grasp_pose
float64[] pre_grasp_dof
float64[] final_grasp_dof
#geometry_msgs/Pose demonstration_pose
int32 TYPE_UNKNOWN = 1
int32 TYPE_FINGERTIP = 2
int32 TYPE_POWER_GRASP = 3        # free grasp
int32 TYPE_TABLECONTACT_GRASP = 4 # finger will make contact w/ table
int32 SPREAD_DOF=0
int32 FINGER_1_DOF=1
int32 FINGER_2_DOF=2
int32 FINGER_3_DOF=3
int32 SOURCE_EIGENGRASPS=1
int32 SOURCE_HUMAN=2
int32 SOURCE_HUMAN_REFINED=3
int32 SOURCE_TABLETOP_ALIGNED=7

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of postion and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

"""
  # Pseudo-constants
  TYPE_UNKNOWN = 1
  TYPE_FINGERTIP = 2
  TYPE_POWER_GRASP = 3
  TYPE_TABLECONTACT_GRASP = 4
  SPREAD_DOF = 0
  FINGER_1_DOF = 1
  FINGER_2_DOF = 2
  FINGER_3_DOF = 3
  SOURCE_EIGENGRASPS = 1
  SOURCE_HUMAN = 2
  SOURCE_HUMAN_REFINED = 3
  SOURCE_TABLETOP_ALIGNED = 7

  __slots__ = ['epsilon_quality','volume_quality','secondary_qualities','grasp_source','grasp_group','grasp_type','pre_grasp_pose','final_grasp_pose','pre_grasp_dof','final_grasp_dof']
  _slot_types = ['float64','float64','float64[]','int32','int32','int32','geometry_msgs/Pose','geometry_msgs/Pose','float64[]','float64[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       epsilon_quality,volume_quality,secondary_qualities,grasp_source,grasp_group,grasp_type,pre_grasp_pose,final_grasp_pose,pre_grasp_dof,final_grasp_dof

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Grasp, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.epsilon_quality is None:
        self.epsilon_quality = 0.
      if self.volume_quality is None:
        self.volume_quality = 0.
      if self.secondary_qualities is None:
        self.secondary_qualities = []
      if self.grasp_source is None:
        self.grasp_source = 0
      if self.grasp_group is None:
        self.grasp_group = 0
      if self.grasp_type is None:
        self.grasp_type = 0
      if self.pre_grasp_pose is None:
        self.pre_grasp_pose = geometry_msgs.msg.Pose()
      if self.final_grasp_pose is None:
        self.final_grasp_pose = geometry_msgs.msg.Pose()
      if self.pre_grasp_dof is None:
        self.pre_grasp_dof = []
      if self.final_grasp_dof is None:
        self.final_grasp_dof = []
    else:
      self.epsilon_quality = 0.
      self.volume_quality = 0.
      self.secondary_qualities = []
      self.grasp_source = 0
      self.grasp_group = 0
      self.grasp_type = 0
      self.pre_grasp_pose = geometry_msgs.msg.Pose()
      self.final_grasp_pose = geometry_msgs.msg.Pose()
      self.pre_grasp_dof = []
      self.final_grasp_dof = []

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
      _x = self
      buff.write(_struct_2d.pack(_x.epsilon_quality, _x.volume_quality))
      length = len(self.secondary_qualities)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.pack(pattern, *self.secondary_qualities))
      _x = self
      buff.write(_struct_3i14d.pack(_x.grasp_source, _x.grasp_group, _x.grasp_type, _x.pre_grasp_pose.position.x, _x.pre_grasp_pose.position.y, _x.pre_grasp_pose.position.z, _x.pre_grasp_pose.orientation.x, _x.pre_grasp_pose.orientation.y, _x.pre_grasp_pose.orientation.z, _x.pre_grasp_pose.orientation.w, _x.final_grasp_pose.position.x, _x.final_grasp_pose.position.y, _x.final_grasp_pose.position.z, _x.final_grasp_pose.orientation.x, _x.final_grasp_pose.orientation.y, _x.final_grasp_pose.orientation.z, _x.final_grasp_pose.orientation.w))
      length = len(self.pre_grasp_dof)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.pack(pattern, *self.pre_grasp_dof))
      length = len(self.final_grasp_dof)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.pack(pattern, *self.final_grasp_dof))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.pre_grasp_pose is None:
        self.pre_grasp_pose = geometry_msgs.msg.Pose()
      if self.final_grasp_pose is None:
        self.final_grasp_pose = geometry_msgs.msg.Pose()
      end = 0
      _x = self
      start = end
      end += 16
      (_x.epsilon_quality, _x.volume_quality,) = _struct_2d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.secondary_qualities = struct.unpack(pattern, str[start:end])
      _x = self
      start = end
      end += 124
      (_x.grasp_source, _x.grasp_group, _x.grasp_type, _x.pre_grasp_pose.position.x, _x.pre_grasp_pose.position.y, _x.pre_grasp_pose.position.z, _x.pre_grasp_pose.orientation.x, _x.pre_grasp_pose.orientation.y, _x.pre_grasp_pose.orientation.z, _x.pre_grasp_pose.orientation.w, _x.final_grasp_pose.position.x, _x.final_grasp_pose.position.y, _x.final_grasp_pose.position.z, _x.final_grasp_pose.orientation.x, _x.final_grasp_pose.orientation.y, _x.final_grasp_pose.orientation.z, _x.final_grasp_pose.orientation.w,) = _struct_3i14d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.pre_grasp_dof = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.final_grasp_dof = struct.unpack(pattern, str[start:end])
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
      _x = self
      buff.write(_struct_2d.pack(_x.epsilon_quality, _x.volume_quality))
      length = len(self.secondary_qualities)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.secondary_qualities.tostring())
      _x = self
      buff.write(_struct_3i14d.pack(_x.grasp_source, _x.grasp_group, _x.grasp_type, _x.pre_grasp_pose.position.x, _x.pre_grasp_pose.position.y, _x.pre_grasp_pose.position.z, _x.pre_grasp_pose.orientation.x, _x.pre_grasp_pose.orientation.y, _x.pre_grasp_pose.orientation.z, _x.pre_grasp_pose.orientation.w, _x.final_grasp_pose.position.x, _x.final_grasp_pose.position.y, _x.final_grasp_pose.position.z, _x.final_grasp_pose.orientation.x, _x.final_grasp_pose.orientation.y, _x.final_grasp_pose.orientation.z, _x.final_grasp_pose.orientation.w))
      length = len(self.pre_grasp_dof)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.pre_grasp_dof.tostring())
      length = len(self.final_grasp_dof)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.final_grasp_dof.tostring())
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.pre_grasp_pose is None:
        self.pre_grasp_pose = geometry_msgs.msg.Pose()
      if self.final_grasp_pose is None:
        self.final_grasp_pose = geometry_msgs.msg.Pose()
      end = 0
      _x = self
      start = end
      end += 16
      (_x.epsilon_quality, _x.volume_quality,) = _struct_2d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.secondary_qualities = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      _x = self
      start = end
      end += 124
      (_x.grasp_source, _x.grasp_group, _x.grasp_type, _x.pre_grasp_pose.position.x, _x.pre_grasp_pose.position.y, _x.pre_grasp_pose.position.z, _x.pre_grasp_pose.orientation.x, _x.pre_grasp_pose.orientation.y, _x.pre_grasp_pose.orientation.z, _x.pre_grasp_pose.orientation.w, _x.final_grasp_pose.position.x, _x.final_grasp_pose.position.y, _x.final_grasp_pose.position.z, _x.final_grasp_pose.orientation.x, _x.final_grasp_pose.orientation.y, _x.final_grasp_pose.orientation.z, _x.final_grasp_pose.orientation.w,) = _struct_3i14d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.pre_grasp_dof = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.final_grasp_dof = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_2d = struct.Struct("<2d")
_struct_3i14d = struct.Struct("<3i14d")
