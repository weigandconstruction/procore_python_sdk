# UpdateSegmentOrderBodyUpdatedOrderInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**segment_id** | **int** | Segment ID | 
**position** | **int** | New position for the segment | 

## Example

```python
from procore_sdk.models.update_segment_order_body_updated_order_inner import UpdateSegmentOrderBodyUpdatedOrderInner

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSegmentOrderBodyUpdatedOrderInner from a JSON string
update_segment_order_body_updated_order_inner_instance = UpdateSegmentOrderBodyUpdatedOrderInner.from_json(json)
# print the JSON string representation of the object
print(UpdateSegmentOrderBodyUpdatedOrderInner.to_json())

# convert the object into a dict
update_segment_order_body_updated_order_inner_dict = update_segment_order_body_updated_order_inner_instance.to_dict()
# create an instance of UpdateSegmentOrderBodyUpdatedOrderInner from a dict
update_segment_order_body_updated_order_inner_from_dict = UpdateSegmentOrderBodyUpdatedOrderInner.from_dict(update_segment_order_body_updated_order_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


