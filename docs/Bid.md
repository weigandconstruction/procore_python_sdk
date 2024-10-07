# Bid

Bid

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**bid_package_id** | **int** | Bid Package ID | [optional] 
**bid_package_title** | **str** | Package Title | [optional] 
**bid_form_title** | **str** | Bid Form Title | [optional] 
**awarded** | **bool** | Bid awarded to vendor | [optional] 
**bidders_can_add_line_items** | **bool** | Bidders can add line items | [optional] 
**bid_status** | **str** | This status is combination of the &#x60;invitation_last_sent_at&#x60;, &#x60;is_bidder_committed&#x60;, &#x60;submitted&#x60;, &amp; &#x60;awarded&#x60; values. The &#x60;not_invited&#x60;  status is the same as &#x60;invitation_last_sent_at&#x60; being null,     &#x60;is_bidder_committed&#x60; being null,  &#x60;submitted&#x60; being false, &amp; &#x60;awarded&#x60; not being true. The &#x60;undecided&#x60;    status is the same as &#x60;invitation_last_sent_at&#x60; not being null, &#x60;is_bidder_committed&#x60; being null,  &#x60;submitted&#x60; being false, &amp; &#x60;awarded&#x60; not being true. The &#x60;will_not_bid&#x60; status is the same as &#x60;invitation_last_sent_at&#x60; not being null, &#x60;is_bidder_committed&#x60; being false, &#x60;submitted&#x60; being false, &amp; &#x60;awarded&#x60; not being true. The &#x60;will_bid&#x60;     status is the same as &#x60;invitation_last_sent_at&#x60; not being null, &#x60;is_bidder_committed&#x60; being true,  &#x60;submitted&#x60; being false, &amp; &#x60;awarded&#x60; not being true. The &#x60;submitted&#x60;    status is the same as &#x60;invitation_last_sent_at&#x60; not being null, &#x60;is_bidder_committed&#x60; being true,  &#x60;submitted&#x60; being true,  &amp; &#x60;awarded&#x60; not being true. The &#x60;awarded&#x60;      status is the same as &#x60;invitation_last_sent_at&#x60; not being null, &#x60;is_bidder_committed&#x60; being true,  &#x60;submitted&#x60; being true,  &amp; &#x60;awarded&#x60; being true.  | [optional] 
**company_id** | **int** | Company ID | [optional] 
**invitation_last_sent_at** | **datetime** | Date/time the Bid invitation was last sent | [optional] 
**is_bidder_committed** | **bool** | Bidder committed | [optional] 
**lump_sum_amount** | **float** | Lump sum (overall) amount. It&#39;s an optional parameter when the blind bidding is on. | [optional] 
**lump_sum_enabled** | **bool** | Lump sum bidding enabled | [optional] 
**submitted** | **bool** | Vendor submitted bid | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**due_date** | **datetime** | Due date | [optional] 
**bidder_comments** | **str** | Comments made on bid sheet. It&#39;s an optional parameter when the blind bidding is on. | [optional] 
**bid_requester** | [**BidBidRequester**](BidBidRequester.md) |  | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**bidder_notes** | **str** | Notes. It&#39;s an optional parameter when the blind bidding is on. | [optional] 
**attachments_count** | **int** | Attachment count. It&#39;s an optional parameter when the blind bidding is on. | [optional] 
**recipient_ids** | **List[int]** | Login IDs of all recipients on a bid | [optional] 
**recipient_list** | [**List[BidRecipientListInner]**](BidRecipientListInner.md) | Detailed recipient informations on bid | [optional] 
**recipient_list_with_email_and_number** | **List[str]** | Recipient emails and phone numbers | [optional] 
**mailto** | **str** | Email address associated with creating communications for bid | [optional] 
**bidder_inclusion** | **str** | Inclusion comments made on bid sheet. It&#39;s an optional parameter when the blind bidding is on. | [optional] 
**bidder_exclusion** | **str** | Exclusion comments made on bid sheet. It&#39;s an optional parameter when the blind bidding is on. | [optional] 
**bid_convertible_to_subcontract** | **bool** | Bid Convertible to Subcontract | [optional] 
**bid_convertible_to_purchase_order** | **bool** | Bid Convertible to Purchase Order | [optional] 
**contract_button_disabled_reason** | **str** | Contract button disabled reason | [optional] 
**po_button_disabled_reason** | **str** | Purchase Order button disabled reason | [optional] 
**links** | [**BidLinks**](BidLinks.md) |  | [optional] 
**vendor** | [**BidVendor**](BidVendor.md) |  | [optional] 
**project** | [**BidProject**](BidProject.md) |  | [optional] 
**bid_items** | [**List[BidBidItemsInner]**](BidBidItemsInner.md) | Items | [optional] 
**cost_codes** | [**List[TimecardEntryFullCostCode]**](TimecardEntryFullCostCode.md) | Cost Codes associated with items | [optional] 
**attachments** | [**List[BidAttachmentsInner]**](BidAttachmentsInner.md) | Attachments. To upload attachments you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with &#x60;attachments[]&#x60; as files. | [optional] 
**attachments_zip_streaming_url** | **str** | Streaming URL to download all attachments. It&#39;s an optional parameter when the blind bidding is on. | [optional] 

## Example

```python
from procore_sdk.models.bid import Bid

# TODO update the JSON string below
json = "{}"
# create an instance of Bid from a JSON string
bid_instance = Bid.from_json(json)
# print the JSON string representation of the object
print(Bid.to_json())

# convert the object into a dict
bid_dict = bid_instance.to_dict()
# create an instance of Bid from a dict
bid_from_dict = Bid.from_dict(bid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


